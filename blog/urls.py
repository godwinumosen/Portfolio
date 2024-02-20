from django.urls import path
from . import views
from .views import add_post


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('new_user_login/', views.login, name='new_user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('second_detail/<int:pk>/', views.second_detail_view, name='detail_second'),
    #path('add_post/', add_post.as_view(), name='add_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('about_author/', views.about_author, name='about_author'),
    path('author_info/', views.author_info, name='author_info'),
    path('update/<int:blog_id>/', views.update_post, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_post, name='delete_blog'),
    
]