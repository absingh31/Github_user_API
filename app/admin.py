# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import User_info

class User_infoAdmin(admin.ModelAdmin):
    list_display = ["Thumbnail","username", "name", "date_searched"] # Email not displayed as it's null for many users
    search_fields = ['name', 'date_searched']                        # Search user based on name and date_searched

    class Meta:
        model = User_info

admin.site.register(User_info, User_infoAdmin)
