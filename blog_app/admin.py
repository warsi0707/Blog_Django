from django.contrib import admin
from .models import Post, contactUs, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(contactUs)
admin.site.register(Comment)
