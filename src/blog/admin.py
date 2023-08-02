# blog/admin.py
from django.contrib import admin
from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'user']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['user']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(User, UserAdmin)  # @admin.register() performs the same function as admin.site.register()
