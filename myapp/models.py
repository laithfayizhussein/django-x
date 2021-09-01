from django.db import models
from django.contrib.auth import get_user_model 
from  django.urls import reverse

# Create your models here.
class Myapp(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    purchaser = models.ForeignKey( get_user_model(),related_name='myapp',on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('myapp_detail', args=[str(self.id)])
    
    def __str__ (self):
        return self.name