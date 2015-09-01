# coding=utf-8
from __future__ import unicode_literals

from rest_framework.views import APIView as BaseAPIView

from .models import Token
from .serializers import AuthTokenSerializer
from .response import success


class ObtainAuthToken(BaseAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = AuthTokenSerializer

    def post(self, request):
        """
        获取token
         ---
        parameters:
            - name: username
              description: username
              required: true
              type: string
              defaultValue: apitest
            - name: password
              description: password
              required: true
              type: string
              defaultValue: apitest
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {'token': token.key, 'expire_time': token.expire_time}
        return success(data)


obtain_auth_token = ObtainAuthToken.as_view()
