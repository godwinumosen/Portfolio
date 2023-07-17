from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('new_user_login/', views.login, name='new_user_login'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('add_post/', views.add_post, name='add_post'),
    
]