from django.db import models

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField() 

class Author(models.Model):
   f_name =  models.CharField(max_length=100)
   surname = models.CharField(max_length=100)
   l_name = models.CharField(max_length=100)
   mobile = models.CharField(max_length=30) 
   email = models.CharField(max_length=30)
      

