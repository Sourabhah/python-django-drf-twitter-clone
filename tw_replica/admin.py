from django.contrib import admin
from .models import UserManagement
from tw_replica.models import Post
# Register your models here.
admin.site.register(UserManagement)
admin.site.register(Post)
