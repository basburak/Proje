from django.contrib import admin

from base.views import room
from .models import Room,Topic,Massage

# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Massage)
