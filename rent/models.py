from django.db import models

# Create your models here.

class jewellery(models.Model):
    groupid=models.IntegerField()
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    category=models.CharField(max_length=100)
    rental_price=models.IntegerField()
    retail_price=models.IntegerField()
    image=models.ImageField(null=True,blank=True)

    def _str_(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class group(models.Model):
    groupid=models.ForeignKey(jewellery,on_delete=models.CASCADE)
    productid=models.IntegerField()

    def _str_(self):
        return self.groupid

class users(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=10)
    email=models.CharField(max_length=500)
    
    def _str_(self):
        return self.username

