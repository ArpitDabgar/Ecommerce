from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.contrib import messages

# Create your views here.

def home(request):
    return HttpResponse("Hello Arpit :) ")

def index(request):
    pid=Product.objects.all()[:4]
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    
    con={"pid":pid,"wish_count":wish_count,"cart_count":cart_count}
    
    return render(request, "index.html",con)

def filter_price(request):
    
    if request.POST:
        max1=request.POST["max1"]
        pid=Product.objects.filter(price__lte=max1)
        
        con={"max1":max1,"pid":pid}
        
        return render(request, "shop.html",con)  

def wishlist(request):
    wish_id=Add_to_Wishlist.objects.all()
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    con={"wish_id":wish_id,"wish_count":wish_count,"cart_count":cart_count}
    return render(request, "wishlist.html",con)

def add_wishlist(request,id):
    pid=Product.objects.get(id=id)
    
    wish_item = Add_to_Wishlist.objects.filter(product_id=pid).first()
    
    if wish_item:
        wish_item.delete()
        messages.info(request, "Item Removed From Your Wishlist")
        return redirect("shop")
        
    else:
        Add_to_Wishlist.objects.create(
            product_id=pid,
            price=pid.price,
            name=pid.name,
            image=pid.image
        )
        messages.info(request, "Item Added To Your Wishlist")
        return redirect("shop")

def delete_wishlist(request,id):
    dell=Add_to_Wishlist.objects.get(id=id)
    dell.delete()
    return redirect("wishlist")

def cart(request):
    cate_id=Add_to_cart.objects.all()
    cart_count=Add_to_cart.objects.all().count()
    wish_count=Add_to_Wishlist.objects.all().count()
    
    total_price=0
    for i in cate_id:
        total_price += i.product_id.price*i.quantity
    
    shipping_charge=50
    
    if total_price==0:
        shipping_charge=0
    else:
        shipping_charge=50
        
    grand_total=total_price+shipping_charge
    
    con={"cate_id":cate_id,"wish_count":wish_count,"cart_count":cart_count,"total_price":total_price,"grand_total":grand_total,"shipping_charge":shipping_charge}
    return render(request, "cart.html",con)

def add_cart(request,id):
    pid=Product.objects.get(id=id)
        
    cart_item = Add_to_cart.objects.filter(product_id=pid).first()
    
    if cart_item:
        cart_item.quantity += 1
        cart_item.total_price = cart_item.quantity * cart_item.price
        cart_item.save()
    
    else:
        Add_to_cart.objects.create(
            product_id=pid,
            price=pid.price,
            name=pid.name,
            quantity=1,
            image=pid.image,
            total_price=pid.price
        )

    return redirect("shop")
    
def cart_decrement(request,id):
    cart=Add_to_cart.objects.get(id=id)
    
    if cart:
        if(cart.quantity==1):
            Add_to_cart.objects.get(id=id).delete()
            
            return redirect("cart")

        else:
            cart.quantity -= 1
            cart.total_price = cart.quantity * cart.price
            cart.save()
            
            return redirect("cart")
        return redirect("cart")
    else:
        return redirect("cart")
    
def cart_increment(request,id):
    
    cart=Add_to_cart.objects.get(id=id)
    
    if cart:
        cart.quantity += 1
        cart.total_price = cart.quantity * cart.price
        cart.save()
        
        return redirect("cart")
    
    else:
        return redirect("cart")
    
def cart_delete(request,id):
    dell=Add_to_cart.objects.filter(id=id)
    dell.delete()
    return redirect("cart")
    
def checkout(request):
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    
    con={"wish_count":wish_count,"cart_count":cart_count}
    return render(request, "checkout.html",con)

def contact(request):
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    
    con={"wish_count":wish_count,"cart_count":cart_count}
    
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        if name and email and message:
        
            Contact.objects.create(name=name,email=email,message=message)
            return redirect("index")
    
    return render(request, "contact.html",con)

def error(request):
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    
    con={"wish_count":wish_count,"cart_count":cart_count}
    return render(request, "error.html",con)

def shop_detail(request):
    return render(request, "shop_detail.html")

def shop_detail1(request,id):
    
    pid=Product.objects.get(id=id)
    con={"pid":pid}
    
    return render(request, "shop_detail.html",con)

def shop(request):
    pid=Product.objects.all().order_by("-id")
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    cat=request.GET.get("cat")
    cid=Category.objects.all()
    sort=request.GET.get('sort')
    wishlist_product=Add_to_Wishlist.objects.all()
    l1=[]
    for i in wishlist_product:
        l1.append(i.product_id.id)
    
    if cat:
        pid=Product.objects.filter(cate_id=cat)
        
    elif sort=="price_asc":
        pid=Product.objects.all().order_by("price")
        
    elif sort=="price_desc":
        pid=Product.objects.all().order_by("-price")
    elif sort=="name_asc":
        pid=Product.objects.all().order_by("name")
    elif sort=="name_desc":
        pid=Product.objects.all().order_by("-name")       
    else:
        pid=Product.objects.all().order_by("-id")

    con={"cid":cid,
         "pid":pid,
         "cat":cat,
         "sort":sort,
         "wish_count":wish_count,
         "cart_count":cart_count,
         "wishlist_product":wishlist_product,
         "l1":l1}
    return render(request,"shop.html",con)


def testimonial(request):
    wish_count=Add_to_Wishlist.objects.all().count()
    cart_count=Add_to_cart.objects.all().count()
    
    con={"wish_count":wish_count,"cart_count":cart_count}
    return render(request, "testimonial.html",con)

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password != confirm_password:
            er={'msg': "Password and Confirm Password don't match"}
            return render(request, "register.html",er)
        
        else :
            User.objects.create(name=name,email=email,password=password)
            return redirect("login")
         
    return render(request, "register.html")

def login(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        
        if email and password:
            try: 
                User.objects.get(email=email,password=password)
                return redirect("index")
            
            except:
                er={'msg': "Invalid Email Or Password"}
                return render(request, "login.html",er)
        
    return render(request, "login.html")

import random
from django.core.mail import send_mail

def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(100000,999999)
        try:
            uid=User.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail(
                "django",
                f"Your OTP Is - {otp}",
                'arpitdabgar009@gmail.com',
                 [email]
                 )
            contaxt={
                "email":email
            }
            return render(request,"confirm_password.html",contaxt)
        except:
            print("Invalid Email")       
            return render(request,"forgot_password.html") 
    else:
        return render(request,"forgot_password.html")

def confirm_password(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        
        try:
            uid=User.objects.get(email=email)
            if str(uid.otp)==otp:
                er={'msg':"Valid OTP"}
                
                if new_password==confirm_password:
                    uid.password=new_password
                    uid.save()
                    er={'msg':"Password Updated"}
                    return redirect("login")
                
                else :
                    er={"msg":"New Password and Confirm Password don't match"}
                    return render(request,"confirm_password.html",er)
                
            elif str(uid.otp) != otp: 
                er = {"msg":"invalid otp"}
                return render(request,"confirm_password.html",er)
            
        except:
            except1 = {"except msg":"except block"}
            return render(request,"confirm_password.html",except1)
                    
    return render(request,"confirm_password.html")

