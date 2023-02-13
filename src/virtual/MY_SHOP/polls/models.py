from django.db import models
from django.db.models.deletion import CASCADE
#from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.utils import timezone


class StoreCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='store')
    pub_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='item')

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User,related_name='user',related_query_name="users_customer", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customers/avatars/')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class StoreOwner(models.Model):
    user = models.ForeignKey(User,related_name='users',related_query_name="users", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customers/avatars/')
    registered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user


class Store(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(StoreOwner, related_name='owners',on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory,related_name='store_category',related_query_name="store_category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    customer = models.ForeignKey(Customer,related_name='customers_MYBAG',related_query_name="customers_MYBAG", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=1000,decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.customer

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name='customers',related_query_name="customers", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.customer