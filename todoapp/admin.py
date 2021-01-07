from django.contrib import admin

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

from .models import Todo
admin.site.register(Todo, TodoAdmin)
