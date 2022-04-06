from dataclasses import fields
from django.contrib import admin
from .models import Post, Comment, IPAddress
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    fields = ['title', 'body','hits',]
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(IPAddress)