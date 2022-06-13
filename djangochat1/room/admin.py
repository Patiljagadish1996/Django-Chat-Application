from django.contrib import admin
from .models import Room

# Register your models here.

admin.site.register(Room)
admin.site.site_header = 'DJANGOCHAT1'
admin.site.index_title = 'ChatApplication'
admin.site.site_title = 'Django'
