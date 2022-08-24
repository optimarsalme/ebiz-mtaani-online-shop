from django.contrib import admin
from .models import Fashion, Electronics, Mainview 
# Register your models here.
class ElectronicsAdmin(admin.ModelAdmin):
    list_display        = ("name", "category", "price")
class FashionAdmin(admin.ModelAdmin):
    list_display        = ("name", "category", "color", "price")  
admin.site.register(Fashion, FashionAdmin)
admin.site.register(Electronics, ElectronicsAdmin)
admin.site.register(Mainview)
    