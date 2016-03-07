from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name="Full name", max_length=150)
    phone = models.CharField(verbose_name="Phone", max_length=50)
