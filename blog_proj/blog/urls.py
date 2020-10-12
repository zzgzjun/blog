from django.conf.urls import  url
from . import views
import blog

urlpatterns = [
    url(r'^index/$', views.index),
]
