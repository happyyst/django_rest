# -*- coding: utf-8 -*-

__author__ = 'Kinslayer'

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from apps.api.common.response import success
from apps.api.common.decorators import token_required, token_optional
from apps.api.common.authentication import TokenAuthentication


class TestAPIView(APIView):
    authentication_classes = (TokenAuthentication,)

    @token_required
    def get(self, request):
        """
        测试token required接口
         ---

        """
        data = {
            'user': str(self.request.user)
        }
        return success(data)

    def post(self, request):
        """
        测试无需token接口
        ---
        parameters:
            - name: name
              description: name
              required: false
              type: string
              paramType: query

        """
        data = {
            'user': str(self.request.user)
        }
        return success(data)

    @token_optional
    def delete(self, request):
        """
        测试token optional接口
        ---
        parameters:
            - name: name
              description: name
              required: false
              type: string
              paramType: query

        """
        data = {
            'user': str(self.request.user)
        }
        return success(data)


@api_view(['GET'])
def test_wrapped(request):
    """
    测试无token验证
    ---
    parameters:
        - name: name
          description: name
          required: false
          type: string
          paramType: query

    """
    data = {
        'user': str(request.user)
    }
    return success(data)


@token_required
@api_view(['GET'])
def test_required(request):
    """
    测试token required
    ---
    parameters:
        - name: name
          description: name
          required: false
          type: string
          paramType: query

    """
    data = {
        'user': str(request.user)
    }
    return success(data)


@token_optional
@api_view(['GET'])
def test_optional(request):
    """
    测试token optional
    ---
    parameters:
        - name: name
          description: name
          required: false
          type: string
          paramType: query

    """
    data = {
        'user': str(request.user)
    }
    return success(data)
