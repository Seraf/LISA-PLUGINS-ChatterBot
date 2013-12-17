from django.conf.urls import patterns, url
from ChatterBot.web import views

urlpatterns = patterns('',
    url(r'^$',views.index),
)
