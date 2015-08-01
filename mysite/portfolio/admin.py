from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Map, Project, Publication

class MapInline(admin.StackedInline):
    model = Map
    extra = 3

class ProjectAdmin(admin.ModelAdmin):

    inlines = [MapInline]

admin.site.register(Map)
admin.site.register(Publication)
admin.site.register(Project, ProjectAdmin)