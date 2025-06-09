from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    password=models.CharField(blank=True,null=True)
    otp=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Product(models.Model):
    cate_id=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    des=models.TextField()
    price=models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
class Add_to_Wishlist(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Contact(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    message=models.TextField()
    
    def __str__(self):
        return str(self.name)
    
class Add_to_cart(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Billing_details(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=20,blank=True,null=True)
    last_name=models.CharField(max_length=20,blank=True,null=True)
    company_name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=20,blank=True,null=True)
    postcode=models.IntegerField(blank=True,null=True)
    mobile=models.IntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    notes=models.TextField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.first_name
    
class Apply_coupon(models.Model):
    code=models.CharField(max_length=200,blank=True,null=True)
    discount=models.IntegerField()
    
    def __str__(self):
        return self.code
    