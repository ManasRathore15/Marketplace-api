from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name= "ads")

    image = models.ImageField(upload_to='ads/', null=True, blank=True)

    def __str__(self):
        return self.title
    
