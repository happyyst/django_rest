import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.timezone import now

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True, unique=True)
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='auth_token')
    expire_time = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    @property
    def expired(self):
        if not self.expire_time:
            return False
        return self.expire_time < now()

    def __str__(self):
        return self.key
