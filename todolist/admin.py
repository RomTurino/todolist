from django.contrib import admin
from todolist.models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('published',)


admin.site.register(Todo, TodoAdmin)
