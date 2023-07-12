from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BlogMode  (models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    img = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title
    
class ProfileMode  (models.Model):
    profile_name = models.CharField(max_length=250)
    profile_content = models.TextField()
    profile_img = models.ImageField(upload_to='profile_images/')
  
    def __str__(self) :
        return self.profile_name

class UserModel(models.Model):
    fistname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length= 100 )
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.fistname