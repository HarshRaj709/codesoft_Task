from django.contrib import admin
from .models import AddTask

@admin.register(AddTask)
class AdminAddTask(admin.ModelAdmin):
    list_display = [field.name for field in AddTask._meta.fields if field.name != 'description'] + ['short_description']
    
    def short_description(self, obj):
        return obj.description[:50]+'...'
    short_description.short_description = 'Description'
