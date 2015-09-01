# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'

from functools import wraps

from django.utils.decorators import available_attrs

"""
提供token认证的装饰器
装饰器顺序十分重要!

class XXXApiView(ApiView):
    @token_optional
    def get(request):
        pass

@token_optional
@api_view
def api_method(request):
    pass

"""


def token_required(view_func):
    """
    用户必须提供token才能访问
    :param view_func:
    :return:
    """

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    setattr(wrapped_view, 'token_required', 'required')
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)


def token_optional(view_func):
    """
    用户提供token时候, 使用token认证, 否则作为AnonymousUser
    :param view_func:
    :return:
    """

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    setattr(wrapped_view, 'token_required', 'optional')
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
