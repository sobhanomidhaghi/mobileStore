from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Banner)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Brand)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'status')
    list_editable = ('status',)


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price')


admin.site.register(ProductAttribute, ProductAttributeAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')


admin.site.register(Color, ColorAdmin)
