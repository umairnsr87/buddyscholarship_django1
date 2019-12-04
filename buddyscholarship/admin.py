from django.contrib import admin
from .models import blog,college,cities
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_type', 'blog_author_name','publish_date')
    list_filter = ("blog_title",'blog_type', 'blog_author_name','publish_date')
    search_fields = ['blog_title', 'blog_type','blog_author_name']
    prepopulated_fields = {'blog_title': ('blog_type','blog_author_name')}

admin.site.register(blog,PostAdmin)


admin.site.register(college)