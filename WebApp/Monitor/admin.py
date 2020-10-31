from django.contrib import admin

# Register your models here.

from .models import SensorNode, Sensor

admin.site.register(SensorNode)
admin.site.register(Sensor)
