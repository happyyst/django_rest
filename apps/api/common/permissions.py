# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

from .utils import token_required_attr

__author__ = 'Kinslayer'


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if token_required_attr(view, request.method) == 'required':
            return request.user and request.user.is_authenticated()
        else:
            return True
