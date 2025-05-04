from django.contrib import admin
from .models import *
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

