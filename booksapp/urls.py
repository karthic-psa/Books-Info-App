from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^all_books/', views.BooksView.as_view(), name='all_books'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^language/', views.LanguageView.as_view(), name='language'),
    url(r'^author/', views.AuthorView.as_view(), name='author'),
    url(r'^(?P<language>[a-zA-Z0-9!@#$&()\-`.+, ]*)/$', views.LanguageDetailView.as_view(), name='book_lang'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
