from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#extending user to Usermanagement to add other features



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to = user_directory_path,blank=True)
    bio = models.TextField(max_length=200,blank=True)
    doj = models.DateField(auto_now_add=True,blank=True)
    dob = models.DateField(blank=True)


    def __str__(self):
        return str(self.user.username)
