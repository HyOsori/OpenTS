from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^result/', views.result, name = 'result'),
    url(r'^crawl/', views.crawl, name = 'crawl'),
    url(r'^getshcode/', views.getshcode, name='getshcode')
]