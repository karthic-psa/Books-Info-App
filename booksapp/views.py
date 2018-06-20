# -*- coding: utf-8 -*-
import datetime
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from models import Language, Books


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Language.objects.all()