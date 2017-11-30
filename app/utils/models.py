from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.helpers.models import BaseModel
from .managers import LikeDislikeManager


class LikeDislike(BaseModel):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (LIKE, _('Like')),
        (DISLIKE, _('Dislike'))
    )

    vote = models.IntegerField(
        verbose_name='vote',
        choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=4000)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()