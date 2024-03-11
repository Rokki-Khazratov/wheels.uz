from django.contrib import admin
from .models import *



class WheelImageAdmin (admin.StackedInline):
    model = WheelImages


@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
    inlines = [WheelImageAdmin]
    list_display = ['name','id']

    class Meta:
        model = Wheel

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name','id','is_checked','adress']

    class Meta:
        model = Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','id']

    class Meta:
        model = Category

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['size','id','width','length']

    class Meta:
        model = Detail