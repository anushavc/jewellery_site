
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class jewellery(models.Model):
    groupid=models.IntegerField()
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    category=models.CharField(max_length=100)
    rental_price=models.IntegerField()
    retail_price=models.IntegerField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class order(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=100,null=True)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(jewellery,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.product.retail_price*self.quantity
        return total

class shippingaddress(models.Model):
    user=models.ForeignKey(users,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.city