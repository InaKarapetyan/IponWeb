from django.db import models
from django.db.models.deletion import CASCADE
#from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100, blank=True, null=True)


class StoreCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='store')
    pub_date = models.DateTimeField(default = timezone.now)


class ItemCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='item')


class Customer(models.Model):
    user = models.ForeignKey(User,related_name='user',related_query_name="users_customer", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customers/avatars/')
    registered_at = models.DateTimeField(auto_now_add=True)


class StoreOwner(models.Model):
    user = models.ForeignKey(User,related_name='users',related_query_name="users", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customers/avatars/', null = True, blank = True)
    registered_at = models.DateTimeField(auto_now_add=True)



class Store(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(StoreOwner, related_name='owners',on_delete=models.CASCADE, null =True)
    store_category = models.ForeignKey(StoreCategory,related_name='store_category',related_query_name="store_category", on_delete=models.CASCADE)

    


class Item(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='store')
    category = models.ForeignKey(ItemCategory,related_name='store_category',related_query_name="store_category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=200,decimal_places=2, blank=True, null=True)
    info = models.CharField(max_length = 1000, blank=True, null=True)
    store = models.ForeignKey(Store,related_name='stores',related_query_name="stores", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MyBug(models.Model):
    customer = models.ForeignKey(Customer,related_name='customers_MYBAG',related_query_name="customers_MYBAG", on_delete=models.CASCADE, null =True)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=1000,decimal_places=1, blank=True, null=True)

    def calculate_total_price(items):
        total_price = sum(item.price for item in items)
        return total_price


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name='customers',related_query_name="customers", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    
    @property
    def total_price(self):
        total = 0
        for i in Item.objects.filter(purchase__id = self.id):
            total +=i.price
        return total