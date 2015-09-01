# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'

default_app_config = 'apps.api.common.config.CommonConfig'
import rest_framework_swagger.introspectors

from . import introspectors


def patch():
    rest_framework_swagger.introspectors.APIViewMethodIntrospector = \
        introspectors.APIViewMethodIntrospector
    rest_framework_swagger.introspectors.WrappedAPIViewMethodIntrospector = \
        introspectors.WrappedAPIViewMethodIntrospector


patch()
