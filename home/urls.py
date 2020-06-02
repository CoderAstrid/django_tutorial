from django.conf.urls import url
from django.urls import path 
from home import views
 
urlpatterns = [
    path('', views.index),
    url(r'^contact', views.contact),
    url(r'^about', views.about),
]