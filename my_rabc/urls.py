from django.conf.urls import url, include

from my_rabc.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login/', login, name="login"),
]
