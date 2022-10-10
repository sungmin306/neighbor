from django.contrib import admin
from .models import Account, Post, comment
# Register your models here.

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(comment)
