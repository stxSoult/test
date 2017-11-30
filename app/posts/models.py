import os
import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.conf import settings

from app.utils.models import LikeDislike, Comment
from app.helpers.models import BaseModel


def picture_upload(instance, filename):
    """ upload picture """
    fn, fext = os.path.splitext(filename)
    fn = 'post-image'
    return '/'.join(['posts', f'{fn}-{str(uuid.uuid4())}{fext}'])


class Post(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET('Deleted User'))
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to=picture_upload)

    votes = GenericRelation(LikeDislike)

    comments = GenericRelation(Comment)

    def __str__(self):
        return str(self.pk)


    class Meta:
        ordering = ['-created_at']