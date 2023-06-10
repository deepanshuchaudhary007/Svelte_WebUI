from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime
from dateutil import parser
from django.views.decorators.csrf import csrf_exempt

from Svelte_Web.services.cart_services import cart_item_remove, get_cart_details, user_cart_id
from .decorators import required_login
from .services.products_service import get_all_category, get_all_products, product_on_category, products_details
from .services.user_services import get_city, get_country, get_state, link_for_forgot_password, password_change, user_login, user_logout, user_profile, user_register

def state(request, id):
    state =[]
    state = get_state(id)
    return HttpResponse(state, status=200)

def city(request, id):
    city =[]   
    city = get_city(id)
    return HttpResponse(city, status=200)

@required_login
def blog_single(request):       
    return render(request, 'blog-single.html')

@required_login
def blog(request):       
    return render(request, 'blog.html')

def cart(request):
    cart_id = request.session['cart_id'] if 'cart_id' in request.session else None
    response =get_cart_details(cart_id) 
    print("Cart details", response) 
    if 'data' in response:
        if 'data' in response:    
            context = {
                "cart_details" : response['data'][0] if 'data' in response else []
            }
            return render(request, 'cart.html', context)
    return render(request, 'cart.html')    

@required_login
def checkout(request):       
    return render(request, 'checkout.html')

def contact_us(request):       
    return render(request, 'contact-us.html')

@required_login
def index(request):   
    all_products = get_all_products()
    if all_products['data']:
        context ={
            "all_products": all_products['data'] if 'data' in all_products else {},
        }   
        return render(request, 'index.html', context)    
    return render(request, 'index.html')


def login(request):   
    country = get_country()  
    if request.method == 'POST':
        message = "Login successfully" 
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        response = user_login(email, password) 
        print(response)   
        if response:  
            if response is None or response['message'] != 'Login Successfully':
                print(response['message'])
                message = "User name  and password are incorrect"
                return render(request, 'login.html', {"message":message} )
            request.session['login_time'] = response['login_time']
            request.session['user_name'] = response['user_info'][0]['name']
            request.session['user_code'] = response['user_info'][0]['user_code']
            request.session['access_token'] = response['token']['access']
            request.session['refresh_token'] = response['token']['refresh']
            cart_info = user_cart_id(response['user_info'][0]['user_code'])  
            request.session['cart_id'] = cart_info['data'][0]['user_cart']['id'] if cart_info['data'][0]['user_cart'] else None              
            return redirect('/')
        return render(request, 'login.html',  {"country": country, "message": "User is email or password incorrect"})
    else:             
        return render(request, 'login.html',  {"country": country})

def register_user(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country_dropdown')
        state = request.POST.get('state_dropdown')
        city = request.POST.get('city_dropdown')
        pin_code = request.POST.get('pin_code')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        data={
            "name":name,
            "email":email,
            "mobile":mobile,
            "address":address,
            "country":country,
            "state":state,
            "city":city,
            "pin_code":pin_code,
            "password":password,
            "password2":password2
        }
        response = user_register(data)
        print(response.json())
        country = get_country()
        return render(request, 'login.html',  {"response": response, "country": country}) 
    country = get_country()      
    return render(request, 'login.html',  {"country": country}) 

@required_login
def change_password(request):   
    country = get_country()  
    if request.method == 'POST':
        message = "Password Changed successfully" 
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        data ={'password': password, 'password2': password2}
        token = request.session['access_token']
        response =password_change(data, token)
        if response:
            if response['message'] == 'Your password changed successfully':                
                del request.session['login_time'] 
                del request.session['user_name'] 
                del request.session['user_code'] 
                del request.session['access_token']
                del request.session['refresh_token']
                user_logout()
                return redirect('/')
        print(response)                 
        return redirect('/')
    else:             
        return render(request, 'login.html',  {"country": country})
    
@required_login
def forgot_password_link(request):   
    country = get_country()  
    if request.method == 'POST':        
        email = request.POST.get('email')
        data ={'email': email}
        response =link_for_forgot_password(data)
        request.session['link'] =response['link']                     
        return render(request, 'forgot_password.html')
    else:             
        return render(request, 'login.html',  {"country": country}) 
    
def password_reset(request, uid, token):  
    country = get_country()  
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        data ={'password': password, 'password2': password2}        
        response =password_change(data, uid, token)
        if response:
            del request.session['link']
            return render(request, 'login.html',  {"country": country})
    return render(request, 'login.html',  {"country": country})
        
   
def logout(request):
    del request.session['login_time'] 
    del request.session['user_name'] 
    del request.session['user_code'] 
    del request.session['access_token']
    del request.session['refresh_token']
    user_logout()       
    return redirect('/login/')

def product_details(request, slug): 
    product_details = products_details(slug) 
    if product_details['data']:
        product_details =product_details['data'][0]
        print(product_details)
        context ={
            "product_details": product_details
        }       
        return render(request, 'product-details.html', context)
    return render(request, 'product-details.html')

def category_filter(request, slug):
    product_details = product_on_category(slug)
    print(product_details) 
    if product_details['data'][0]['product']:
        product_details = product_details['data'][0]['product'] if 'product' in product_details['data'][0] else {}
        context ={
            "product_details": product_details
        }       
        return render(request, 'category_base_product.html', context)
    return render(request, 'category_base_product.html')

@required_login
def shop(request):       
    return render(request, 'shop.html')

@required_login
def user_details(request, user_code): 
    user_details = user_profile(user_code) 
    if 'data' in user_details:
        user_info = user_details['data'][0] 
        context ={
            "user_profile": user_info
        }   
        return render(request, 'user_profile.html', context)
    return render(request, 'user_profile.html')

@csrf_exempt
def delete_cart_item(request, id):
    response = cart_item_remove(id)
    


