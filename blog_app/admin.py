from django.contrib import admin
from .models import Title, Tasks
# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'category', 'time']
    list_display_links = ['id', 'description']
    prepopulated_fields = {'slug': ('description',)}


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Title, TitleAdmin)