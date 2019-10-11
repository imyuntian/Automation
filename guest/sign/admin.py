from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.
# 通知Admin管理工具为这些模块逐一提供界面

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
