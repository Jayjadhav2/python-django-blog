from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
# Create your models here.

class Profile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default1.jpg',upload_to='profile_pics')
   
   
    def __str__(self):
        return f'{self.users.username} profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs) # calling parent class save method

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

   