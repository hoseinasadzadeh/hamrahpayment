from django.contrib import admin
from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


class FileAdminInline(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'avatar',
              'description', 'file_type', 'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_categories', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileAdminInline]

    def display_categories(self, obj):
        categories = obj.categories.all()
        if categories:
            return ", ".join([category.title for category in categories])
        return "بدون دسته‌بندی"
    display_categories.short_description = 'دسته‌بندی‌ها'
    display_categories.allow_tags = True  # برای نمایش HTML
