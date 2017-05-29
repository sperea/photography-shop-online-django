from django.contrib import admin
from .models import Category, Product, Coursecategory, Course, ProductSize

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(ProductSize, ProductSizeAdmin)

class CoursecategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Coursecategory, CoursecategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'coursecategory', 'price', 'created', 'updated']
    list_filter = ['created', 'updated', 'coursecategory']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Course, CourseAdmin)

