from django.contrib import admin
from .models import BlogMode
from .models import UserModel


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user','pub_date','img') 
admin.site.register(BlogMode, BlogModelAdmin)

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('fistname', 'lastname', 'email')  
admin.site.register(UserModel, UserModelAdmin)


