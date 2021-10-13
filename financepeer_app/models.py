from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Blog(models.Model):
    userId = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=150)
    body = models.TextField(_("Body"))
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    last_updated_date = models.DateTimeField(_("Last Update date"), auto_now=True)