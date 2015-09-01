from django.contrib.auth import authenticate

from rest_framework import exceptions, serializers


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise exceptions.APIException(msg)
            else:
                msg = 'Unable to log in with provided credentials.'
                raise exceptions.APIException(msg)
        else:
            msg = 'Must include "username" and "password".'
            raise exceptions.APIException(msg)

        attrs['user'] = user
        return attrs
