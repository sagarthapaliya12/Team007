from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',)
    def __str__(self):
        return f'{self.user.email} Profile'