from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ("todo",)

# Register model
admin.site.register(Todo, TodoAdmin)
