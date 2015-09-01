# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.compat import set_rollback

from .response import error


def exception_handler(exc, context):
    if isinstance(exc, exceptions.APIException):
        set_rollback()
        return error(exc.status_code, exc.detail)
    elif isinstance(exc, Http404):
        msg = 'Not found.'
        set_rollback()
        return error(404, msg)
    elif isinstance(exc, PermissionDenied):
        msg = 'Permission denied.'
        set_rollback()
        return error(403, msg)
    return error(500, exc.message)
