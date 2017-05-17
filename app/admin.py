# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib import admin
from .models import User_info

class User_infoAdmin(admin.ModelAdmin):
    list_display = ["Thumbnail","username", "name", "date_searched"] # Email not displayed as it's null for many users
    search_fields = ['name', 'date_searched']                        # Search user based on name and date_searched

    class Meta:
        model = User_info

class report_for_today(User_info):
    class Meta:
        proxy = True

class today(User_infoAdmin):
    def get_queryset(self, requests):
        return self.model.objects.filter(date_searched = datetime.date.today())

class report_for_month(User_info):
    class Meta:
        proxy = True

class month(User_infoAdmin):
    def get_queryset(self, requests):
        return self.model.objects.filter(date_searched__month__lte= datetime.datetime.today().month)

class report_for_year(User_info):
    class Meta:
        proxy = True

class year(User_infoAdmin):
    Updated = datetime.date.today()
    def get_queryset(self, requests):
        return self.model.objects.filter(date_searched__year__lte= datetime.datetime.today().year)

admin.site.register(User_info, User_infoAdmin)
admin.site.register(report_for_today, today)
admin.site.register(report_for_month, month)
admin.site.register(report_for_year, year)


