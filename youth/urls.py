from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^youth/$', views.numbers, name='youth'),
    
)