from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'groups')


admin.site.register(User, UserAdmin)