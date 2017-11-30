from django.contrib import admin

# Register your models here.
from .models import Comment, LikeDislike
admin.site.register(LikeDislike)
admin.site.register(Comment)