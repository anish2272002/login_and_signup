from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    dob=models.DateField()
    gender=models.BooleanField(choices=[(False,'Male'),(True,'Female')],default=False)
    profile_pic=models.ImageField(upload_to='profile',default="../static/img6Q.png",blank=True)
    def __str__(self):
        return "{0} {1}".format(self.user.first_name,self.user.last_name)