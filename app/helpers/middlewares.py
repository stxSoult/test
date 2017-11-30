import os
from django.shortcuts import redirect, reverse
from django.contrib.auth.views import login, logout
from django.contrib import messages


safe_urls = [reverse('accounts:register'),
             reverse('accounts:login'),]


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        user = request.user.is_authenticated()

        if request.user.is_staff:
            return response

        if not user and request.path not in safe_urls:
            messages.error(request, 'Login to browse')
            return redirect('accounts:login')

        if user and not request.user.email_confirmed:
            messages.error(request, 'First activate your email')
            logout(request)

        return response

    return middleware
