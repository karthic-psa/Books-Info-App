# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=140, blank=True, null=True)
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100, default='')
    link = models.URLField(max_length=350)
    pages = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)
    imageLink = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.id, })






