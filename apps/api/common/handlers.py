# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.compat import set_rollback
# from django.core.urlresolvers import resolve
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth.models import User
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


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


def resource_access_handler(request, resource):
    """ Callback for resource access. Determines who can see the documentation for which API. """
    # Get the underlying HttpRequest object
    try:
        # 因为rest frame work使用token认证覆盖了默认的认证方式, 这里通过session来确定文档用户的真实身份
        _auth_user_id = request.session['_auth_user_id']
        user = User.objects.get(id=_auth_user_id)
    except:
        user = None

    # Unauthenticated, CSRF validation not required
    if not user or not user.is_active:
        return False

    reason = CSRFCheck().process_view(request, None, (), {})
    if reason:
        # CSRF failed, bail with explicit error message
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

    # Superusers and staff can see whatever they want
    if user.is_superuser or user.is_staff:
        return True
    else:
        # if isinstance(resource, basestring):
        #     try:
        #         resolver_match = resolve('/{}/'.format(resource))
        #         view = resolver_match.func
        #     except Exception:
        #         return False
        # else:
        #     view = resource.callback
        return False
