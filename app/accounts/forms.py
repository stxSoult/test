from django.contrib.auth.forms import UserCreationForm
from .models import User
import re
from django.forms import SelectDateWidget, DateField
from django.utils import timezone


def date_range(n):
    this_year = timezone.now().year
    return list(range(this_year-n, this_year-4))


class CustomUserCreationForm(UserCreationForm):
    birthday = DateField(widget=SelectDateWidget(years=date_range(70)))
    password2 = None

    class Meta:
        model = User
        fields = ('email', 'password1', 'city', 'country', 'birthday')

    def clean(self):
        data = super(CustomUserCreationForm, self).clean()
        try:
            user = User.objects.get(email__iexact=data.get('email'))
            self.add_error('email', 'User already exists')
        except User.DoesNotExist:
            pass

        return data

