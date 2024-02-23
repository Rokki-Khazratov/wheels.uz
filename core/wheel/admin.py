from django.contrib import admin
from .models import *

admin.site.register(Detail)
admin.site.register(Category)
admin.site.register(UserProfile)
# admin.site.register(Wheel)
# admin.site.register(WheelImages)

class WheelImageAdmin (admin.StackedInline):
    model = WheelImages


@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
    inlines = [WheelImageAdmin]
    #,'category.size'
    list_display = ['name','id']

    class Meta:
        model = Wheel