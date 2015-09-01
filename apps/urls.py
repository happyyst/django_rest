# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'

from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('apps.api.urls'))

]
