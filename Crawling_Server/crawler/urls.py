from django.conf.urls import url
from . import views
import pythoncom
import win32com

urlpatterns = [
    url(r'^crawl/', views.crawl, name = 'crawl'),
    url(r'^getshcode/', views.getshcode, name='getshcode')
]