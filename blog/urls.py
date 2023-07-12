from django.urls import path
from . import views
from blog.views import signup,login

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    
]