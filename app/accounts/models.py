from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from app.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150, unique=True)
    email_confirmed = models.BooleanField(default=False)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
