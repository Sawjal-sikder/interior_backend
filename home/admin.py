from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.



class BanarAdmin(admin.ModelAdmin):
    list_display = ["title","short_description", "is_active"]

admin.site.register(Banar, BanarAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title","description", "is_active"]

admin.site.register(Service, ServiceAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","description","price", "is_active"]

admin.site.register(Product, ProductAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["title","description", "is_active"]
admin.site.register(Portfolio, PortfolioAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name","email", "phone", "message"]
admin.site.register(ContactUs, ContactUsAdmin)



class ClientAdmin(admin.ModelAdmin):
    list_display = ["title","description", "is_active"]
admin.site.register(Client, ClientAdmin)




class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title","description", "rating"]
admin.site.register(Review, ReviewAdmin)




class LatestProjectAdmin(admin.ModelAdmin):
    list_display = ["title","description", "is_active"]
admin.site.register(LatestProject, LatestProjectAdmin)



class ChooseusAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())  # rich text editor

    class Meta:
        model = Chooseus
        fields = '__all__'

class ChooseusAdmin(admin.ModelAdmin):
    form = ChooseusAdminForm
    list_display = ["title", "description", "is_active"]

admin.site.register(Chooseus, ChooseusAdmin)