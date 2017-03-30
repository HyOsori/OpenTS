from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^result/', views.result, name = 'result'),
    url(r'^crawl/', views.Crawling.as_view()),
    url(r'^getshcode/', views.getshcode, name='getshcode')
]