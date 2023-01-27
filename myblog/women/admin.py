from django.contrib import admin

from women.models import Women, Category, Tags


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
