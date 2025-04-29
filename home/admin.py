from django.contrib import admin
from .models import *
# Register your models here.



class BanarAdmin(admin.ModelAdmin):
    list_display = ["title","short_description", "is_active"]

admin.site.register(Banar, BanarAdmin)