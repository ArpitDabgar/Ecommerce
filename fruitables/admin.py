from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(User)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Contact)

admin.site.register(Add_to_cart)

admin.site.register(Add_to_Wishlist)

admin.site.register(Billing_details)

admin.site.register(Apply_coupon)
