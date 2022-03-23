from django.contrib import admin
from .models import Database
# Register your models here.
class User(admin.ModelAdmin):
    list_display = ['temperature', 'date_added']
admin.site.register(Database, User)