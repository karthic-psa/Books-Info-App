# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'author', 'country', 'year', 'count', 'pages', 'link', 'imageLink')
    list_filter = ('language',)
    ordering = ('title',)


admin.site.register(Books, BooksAdmin)