from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.

class CommectInline(admin.TabularInline):#(admin.StackedInline):
    model = Comment
    list_display = ['author', 'body','date']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommectInline]

admin.site.register(Post, PostAdmin)
