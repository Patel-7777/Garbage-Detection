from django.db import models

# Create your models here.
class Pictures(models.Model):
    
    imgs=models.ImageField(upload_to='images')