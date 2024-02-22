from django.contrib import admin
from .models import *

admin.site.register(Category)
# admin.site.register(Wheel)
# admin.site.register(WheelImages)

class WheelImageAdmin (admin.StackedInline):
    model = WheelImages


@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
    inlines = [WheelImageAdmin]
    list_display = ['name','id','size','price','climate']

    class Meta:
        model = Wheel