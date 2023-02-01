from django.db import models
import datetime


# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="Piyush Pawar")
    address = models.CharField(max_length=150,default=" Indore")
    phone = models.IntegerField(default='+91 9131721743')

    def __str__(self):
        return self.name
   
class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    purchase_date = models.DateField(default=datetime.datetime.now)
    #purchase_date = models.DateField(auto_now=True)

class product(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)

class Contact(models.Model):
    email= models.CharField(max_length=120,null=True)
    Name=models.CharField(max_length=120,null=True)
    LastName=models.CharField(max_length=120,null=True)
    city = models.CharField(max_length=120,null=True)



   
