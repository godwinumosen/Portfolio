from django.contrib import admin
from .models import BlogMode



class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user','pub_date','img') 
admin.site.register(BlogMode, BlogModelAdmin)



