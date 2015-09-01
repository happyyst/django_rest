# -*- coding: utf-8 -*-


__author__ = 'Kinslayer'

from django.http import JsonResponse as Response
# from rest_framework.response import Response


def success(data):
    return Response({'code': 200, 'data': data})


def error(code, msg):
    return Response({'code': code, 'msg': msg})
