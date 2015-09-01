# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import resolve
from rest_framework.authentication import BaseAuthentication

__author__ = 'Kinslayer'

from rest_framework import exceptions
from .models import Token
from .utils import token_required_attr


class TokenAuthentication(BaseAuthentication):
    model = Token

    def authenticate(self, request):

        func, args, kwargs = resolve(request.path)
        token = request.GET.get('token')
        if request.method == 'POST':
            token = token or request.POST.get('token')

        if token:
            return self.authenticate_credentials(token)

        token_required = getattr(func, 'token_required', '') or token_required_attr(func.cls, request.method)

        if token_required == 'required':
            raise exceptions.AuthenticationFailed('No token found')
        else:
            return AnonymousUser(), None

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
        if token.expired:
            raise exceptions.AuthenticationFailed('Token Expired.')
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return token.user, token
