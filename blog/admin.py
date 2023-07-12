from django.contrib import admin
from .models import BlogMode
from .models import UserModel
from .models import ProfileMode

class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user','pub_date','img') 
admin.site.register(BlogMode, BlogModelAdmin)

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('fistname', 'lastname', 'email')  
admin.site.register(UserModel, UserModelAdmin)

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('profile_name','profile_content','profile_img')  
admin.site.register(ProfileMode, ProfileModelAdmin)

