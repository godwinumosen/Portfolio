from django.urls import path
from . import views
from .views import add_post


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('new_user_login/', views.login, name='new_user_login'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    #path('add_post/', add_post.as_view(), name='add_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('about_author/', views.about_author, name='about_author'),
    path('author_info/', views.author_info, name='author_info'),
    path('detail/update/<int:pk>/', views.update_post, name='update_post'),
    
]