from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^all_books/', views.BooksView.as_view(), name='all_books'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^language/', views.LanguageView.as_view(), name='language'),
    url(r'^(?P<language>[a-zA-Z0-9!@#$&()\-`.+, ]*)/$', views.LanguageDetailView.as_view(), name='book_lang'),
]
