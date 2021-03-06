from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index$',index,name='index'),
    url(r'^langs$',langs,name='langs'),
    url(r'^newindex$',new_index),
    url(r'^myindex/(\d+)$',
        myindex_with_param,
        name='myindex_with_param'),
    url(r'^v1_index/(?P<p2>\d+)$',
        myindex_with_param_v1,
        name='myindex_with_param_v1'),
    url(r'new_reverse',
        new_reverse,
        name = 'new_reverse'),
    url(r'^home$',home,name='home')

]