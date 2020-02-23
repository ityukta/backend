from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    
