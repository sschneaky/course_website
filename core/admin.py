from django.contrib import admin

from .models import ClassPeriod, Reading, Event

# Register your models here.

admin.site.register(ClassPeriod)
admin.site.register(Reading)
admin.site.register(Event)