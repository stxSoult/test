from django.db import models
from django.utils.translation import ugettext as _

class BaseModel(models.Model):
    """ABSTRACT MODEL ADD DATES OF CREATION AND UPDATE"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'Creation date'))
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'Edited date')
    )

    objects = models.Manager()

    class Meta:
        abstract = True

    def month_name(self):
        return self.created_at.strftime('%B')[0:3].upper()