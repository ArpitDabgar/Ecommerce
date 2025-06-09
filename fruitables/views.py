from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.contrib import messages
from django.core.paginator import Paginator 
# Create your views here.

def home(request):
    return HttpResponse("Hello Arpit :) ")

def index(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Product.objects.all()[:4]
        wish_count=Add_to_Wishlist.objects.all().count()
        cart_count=Add_to_cart.objects.all().count()
        
        con={"pid":pid,"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        
        return render(request, "index.html",con)
    else:
        return render(request, "login.html")
        

def filter_price(request):
    
    if request.POST:
        max1=request.POST["max1"]
        pid=Product.objects.filter(price__lte=max1)
        
        con={"max1":max1,"pid":pid}
        
        return render(request, "shop.html",con)  

def wishlist(request):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        wish_item = Add_to_Wishlist.objects.filter(user_id=uid)
        
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        con={"wish_item":wish_item,"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        return render(request, "wishlist.html",con)
    else:
        return render(request, "login.html")

def add_wishlist(request,id):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Product.objects.get(id=id)
        
        wish_item = Add_to_Wishlist.objects.filter(product_id=pid).first()
        
        if wish_item:
            wish_item.delete()
            messages.info(request, "Item Removed From Your Wishlist")
            return redirect("shop")
            
        else:
            Add_to_Wishlist.objects.create(
                user_id=uid,
                product_id=pid,
                price=pid.price,
                name=pid.name,
                image=pid.image
            )
            messages.info(request, "Item Added To Your Wishlist")
            return redirect("shop")
    else:
        return render(request, "login.html")

def delete_wishlist(request,id):
    dell=Add_to_Wishlist.objects.get(id=id)
    dell.delete()
    return redirect("wishlist")

def cart(request):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        cart_items = Add_to_cart.objects.filter(user_id=uid)
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        
        total_price=0
       
        for i in cart_items:
            total_price += i.product_id.price*i.quantity
        
        shipping_charge=50
        
        if total_price==0:
            shipping_charge=0
        else:
            shipping_charge=50
             
        grand_total=total_price+shipping_charge
        
        con={"cart_items":cart_items,"wish_count":wish_count,
             "cart_count":cart_count,"total_price":total_price,
             "grand_total":grand_total,"shipping_charge":shipping_charge,
             "uid":uid}
        return render(request, "cart.html",con)
    else:
        return render(request, "login.html")

def add_cart(request,id):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Product.objects.get(id=id)

        cart_item = Add_to_cart.objects.filter(product_id=pid).first()
        
        if cart_item:
            cart_item.quantity += 1
            cart_item.total_price = cart_item.quantity * cart_item.price
            cart_item.save()
        else:
            Add_to_cart.objects.create(
                user_id=uid,
                product_id=pid,
                price=pid.price,
                name=pid.name,
                quantity=1,
                image=pid.image,
                total_price=pid.price
            )

        return redirect("shop")
    
    else:
        return render(request, "login.html")
    
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

def apply_coupon(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        aid= Add_to_cart.objects.filter(user_id=uid)
        wish_count = Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count = Add_to_cart.objects.filter(user_id=uid).count()
        
        
    
    
def checkout(request):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        check_id=Add_to_cart.objects.filter(user_id=uid)
        
        total_price=0
        for i in check_id:
            total_price+=i.product_id.price*i.quantity
        
        con={"wish_count":wish_count,"cart_count":cart_count,"check_id":check_id,"total_price":total_price,"uid":uid}
        return render(request, "checkout.html",con)
    else:
        return render(request, "login.html")

def billing_view(request):
    if 'email' in request.session:
        
        if request.POST:
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            company_name=request.POST['company_name']
            address=request.POST['address']
            city=request.POST['city']
            country=request.POST['country']
            postcode=request.POST['postcode']
            mobile=request.POST['mobile']
            email=request.POST['email']
            notes=request.POST['notes']
            
            
            if first_name and last_name and company_name and address and city and country and postcode and mobile and email and notes:
            
                Billing_details.objects.create(first_name=first_name,last_name=last_name,
                                            company_name=company_name,address=address,
                                            city=city,country=country,postcode=postcode,
                                            mobile=mobile,email=email,notes=notes 
                                            )
                return redirect("checkout")
            
            return render(request, "checkout.html")
        else:
            return render(request, "checkout.html")
        
    else:
        return render(request, "login.html")
    
def contact(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        
        con={"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        
        if request.POST:
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            
            if name and email and message:
            
                Contact.objects.create(name=name,email=email,message=message)
                return redirect("index")
        
        return render(request, "contact.html",con)
    
    else:
        return render(request, "login.html")

def error(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        
        con={"uid":uid,"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        return render(request, "error.html",con)
    
    else:
        return render(request, "login.html")

def shop_detail(request):
    return render(request, "shop_detail.html")

def shop_detail1(request,id):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Product.objects.get(id=id)
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        con={"uid":uid,"pid":pid,"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        
        return render(request, "shop_detail.html",con)
    
    else:
        return render(request, "login.html")

def shop(request):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
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


        paginator=Paginator(pid,3)  
        page_number=request.GET.get("page",2)  
        pid=paginator.get_page(page_number)
        show_page=paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=2)
        
        con={"uid":uid,
            "cid":cid,
            "pid":pid,
            "cat":cat,
            "sort":sort,
            "wish_count":wish_count,
            "cart_count":cart_count,
            "wishlist_product":wishlist_product,
            "show_page":show_page,
            "l1":l1}
        return render(request,"shop.html",con)
    
    else:
        return render(request, "login.html")


def testimonial(request):
    if 'email'in request.session:
        uid=User.objects.get(email=request.session['email'])
        wish_count=Add_to_Wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
    
        con={"uid":uid,"wish_count":wish_count,"cart_count":cart_count,"uid":uid}
        return render(request, "testimonial.html",con)
    else:
        return render(request, "login.html")

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
    if 'email'in request.session:
        return redirect("index")
    else:
        try:
            if request.POST: 
                email=request.POST['email']
                password=request.POST['password']
                uid=User.objects.get(email=email)
                if uid.email==email:
                    request.session['email']=uid.email
                    if uid.password==password:
                        return redirect("index")
                    else: 
                        con={
                            "msg":"Invalid Password"
                        }  
                        return render(request,"login.html",con)
                else:
                    con={
                            "msg":"Invalid Email"
                        }  
                    return render(request,"login.html",con)
            else:
                con={
                            "msg":"Post"
                        }  
                return render(request,"login.html",con)
        except:
            print("except block")
            return render(request,"login.html")

def logout(request):
    
    if 'email' in request.session:
        del request.session['email']
        return render(request,'login.html')
    else:
        return render(request,'login.html')
    
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

