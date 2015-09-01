# coding=utf-8
from django.conf.urls import url, include

from views.test import *  # noqa
from apps.api.common.views import obtain_auth_token

urlpatterns = [
    url(r'', include('rest_framework_swagger.urls')),
    url(r'auth$', obtain_auth_token),
    url(r'test_api_view$', TestAPIView.as_view()),
    url(r'test_wrapped', test_wrapped),
    url(r'test_required', test_required),
    url(r'test_optional', test_optional),
]
