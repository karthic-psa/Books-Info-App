# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Books, Language


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'author', 'country', 'date', 'count', 'pages', 'link', 'img_link')
    list_filter = ('language',)
    ordering = ('title',)


admin.site.register(Language)
admin.site.register(Books, BooksAdmin)