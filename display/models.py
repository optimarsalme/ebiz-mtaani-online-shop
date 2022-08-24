from django.db import models
import datetime

# Create your models here.
class Electronics(models.Model):
    category             = models.CharField(max_length=20, default="TV")
    name                 = models.CharField(max_length=20,default='HD Bravia')
    brand                = models.CharField(max_length=20, default='Sony')
    condition            = models.CharField(max_length=100, default="Brand New")
    size                 = models.IntegerField(default=32)
    posted               = models.DateTimeField('date posted')
    price                = models.IntegerField(default=10000)
    price_text           = models.CharField(max_length=100 ,default="10,000")
    weight               = models.IntegerField(default=4)
    rating               = models.IntegerField(default=1)
    image                = models.ImageField(upload_to="Electronics/", blank='True')
    
    class Meta:
        verbose_name_plural         = "Electronics"
    def __str__(self):
        return self.name
class Fashion(models.Model):
    category                = models.SlugField(max_length=20, default='shirt')
    name                    = models.CharField(max_length=20, default='Casual')
    color                   = models.CharField(max_length=20, default='Black')
    condition               = models.CharField(max_length=100, default="Brand New")    
    price                   = models.IntegerField(default=200)    
    posted                  = models.DateTimeField('date posted')
    price_text              = models.CharField(max_length=100 ,default="500")
    stock                   = models.IntegerField(default=1)
    rating                  = models.IntegerField(default=1)
    image                   = models.ImageField(upload_to='Sweater/', blank=True)
    class Meta:
        verbose_name_plural = "Fashion"
    
    def __str__(self):
        return self.name
    
  
class Mainview(models.Model):
    name                        = models.CharField(max_length=10)
    image                       = models.ImageField(upload_to='mainview/')
    class Meta:
        verbose_name_plural     = "Mainview"
    def __str__(self):
        return self.name
        
    
    