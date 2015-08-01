from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Blog, BlogImage, BlogCitation

class BlogImageInline(admin.StackedInline):
    model = BlogImage
    extra = 3

class BlogCitationInline(admin.StackedInline):
    model = BlogCitation
    extra = 3

class ProjectAdmin(admin.ModelAdmin):

    inlines = [BlogImageInline, BlogCitationInline]

admin.site.register(BlogImage)
admin.site.register(BlogCitation)
admin.site.register(Blog, ProjectAdmin)