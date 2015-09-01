# -*- coding: utf-8 -*-
__author__ = 'Kinslayer'


def token_required_attr(cls, method):
    """
    判断一个class view的某个方法是否需要token
    :param cls: view class
    :param method: GET, POST, ...
    :return:
    required
    optional
    ...
    """
    method = str(method).lower()
    if not hasattr(cls, method):
        return False
    method = getattr(cls, method)
    return getattr(method, 'token_required', '')
