from django.contrib import messages
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import FormView
from datetime import datetime
from .forms import CustomUserCreationForm
from .models import User
from .tokens import email_confirm_token


class CustomRegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect('posts:post-list')
        return super(CustomRegisterView, self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.city = self.request.POST.get('city', '')
        instance.country = self.request.POST.get('country', '')

        y, m, d = (form.data.get('birthday_year'),
                   form.data.get('birthday_month'),
                   form.data.get('birthday_day'))

        instance.birthday = datetime(int(y), int(m), int(d))
        instance.save()

        self.send_email(instance)
        messages.success(
            self.request,
            _(f'Activation instructions were sent to {instance.email}')
        )
        return super(CustomRegisterView, self).form_valid(form)

    def send_email(self, user):
        site = get_current_site(self.request)
        subject = _('Activation instructions.')
        message = render_to_string('accounts/reg_confirm_email.html', {
            'user': user,
            'domain': site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': email_confirm_token.make_token(user),
        })

        user.email_user(subject, message, html_message=message)


class EmailConfirmation(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and email_confirm_token.check_token(user, token):
            user.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, 'Account activated')
            return redirect('accounts:register')
        else:
            # invalid link
            raise Http404