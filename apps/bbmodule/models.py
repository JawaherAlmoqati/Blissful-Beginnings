from django.db import models

class bbWeb(models.Model):
     Makeup_artists= models.CharField(max_length=50)
     Hair_stylists= models.CharField(max_length=50)
     Photographers= models.CharField(max_length=50)
     Bridemaid= models.CharField(max_length=50)  
     Price= models.FloatField(default=0.0)  

