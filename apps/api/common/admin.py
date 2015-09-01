from django.contrib import admin

from .models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'expire_time', 'create_time')
    fields = ('user',)
    ordering = ('-create_time',)


admin.site.register(Token, TokenAdmin)
