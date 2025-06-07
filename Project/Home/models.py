from django.db import models

# Create your models here.
class Product(models.Model):
    first_name = models.CharField(max_length=20)

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=1,
                              choices=[("M","Male"),
                              ("F","Female")])
    profile= models.ImageField('User/Images')
    documents = models.FileField('Documents/Images')
    status = models.BooleanField(default=False)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    website_name = models.URLField()

class Room(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    room_no = models.CharField(max_length=4)