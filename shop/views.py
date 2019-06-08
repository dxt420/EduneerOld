from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
# from cart.cart import Cart
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

from pyrebase import pyrebase
from . models import *
from datetime import datetime

from django.conf import settings


import re
from django.contrib import auth




from django.dispatch import receiver




config = {
    'apiKey': "AIzaSyAd8pc4st2fpBSt92GxeW9iF4Uql3j6LXI",
    'authDomain': "eduneer-82d2e.firebaseapp.com",
    'databaseURL':  "https://eduneer-82d2e.firebaseio.com",
    'projectId': "eduneer-82d2e",
    'storageBucket': "eduneer-82d2e.appspot.com",
    'messagingSenderId': "279848792993",
    'appId' : "1:279848792993:web:4d156db97784ae7b"
 
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()


# PPPPPPPPPPAAAAAAAAAAAAASSSSSSSSSSSSSWWWWWWWWWWWWWWWWWOOOOOOOOOOOOORRRRRRRRRRRRDDDDDDDDDDDDDDD
# eduneeradmin143



# email="admin@mujamall.com"
# passw = "admin123"

# auth.sign_in_with_email_and_password(email,passw)
# 

# user = firebase.auth().currentUser

# user = request.session.get('user')

def login(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"active",
        'cart': cart
    }
    return render(request,"shop/login.html",context)

def register(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"active",
        'cart': cart
    }
    return render(request,"shop/register.html",context)

def completeregister(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"active",
        'cart': cart
    }
    return render(request,"shop/complete-register.html",context)

    

def forgot(request):
    cart = Cart(request)

    
    context = {
       
        "aaaaa":"active",
        'cart': cart
    }
    return render(request,"shop/forgot_password.html",context)


def logout(request):
    # auth.current_user = None
    auth.logout(request)
    # request.user = None
    # request.session['user'] = None
    # request.session['checkout_redirect'] =  None
    # auth.signOut()
    return HttpResponseRedirect(reverse('shop:home'))

def home(request):
    cart = Cart(request)

    # if request.user:
        

    
    context = {
       
        "home_active":"active",
        'cart': cart
    }

    print(request.user)
    print(request.user.is_staff)
    print(authe.current_user)
    # print(auth.current_user)
    if request.user.is_staff:
        return render(request,"shop/admin/dashboard.html",context)
    else:
        return render(request,"shop/home.html",context)
    

def courses(request):
    cart = Cart(request)

    
    context = {
       
        "courses_active":"active",
        'cart': cart
    }
    return render(request,"shop/courses.html",context)

def mycourses(request):
    cart = Cart(request)

    
    context = {
       
        "my_courses_active":"active",
        'cart': cart
    }
    return render(request,"shop/mycourses.html",context)

def coursedetail(request):
    cart = Cart(request)

    
    context = {
       
        "ajs":"active",
        'cart': cart
    }
    return render(request,"shop/course_detail.html",context)

def talkdetail(request):
    cart = Cart(request)

    
    context = {
       
        "ajs":"active",
        'cart': cart
    }
    return render(request,"shop/talk_details.html",context)





def talks(request):
    cart = Cart(request)

    
    context = {
       
        "talks_active":"active",
        'cart': cart
    }
    return render(request,"shop/talks.html",context)

def cart(request):
    cart = Cart(request)

    
    context = {
       
        "cart_active":"active",
        'cart': cart
    }
    return render(request,"shop/cart.html",context)

def news(request):
    cart = Cart(request)

    
    context = {
       
        "news_active":"active",
        'cart': cart
    }
    return render(request,"shop/news.html",context)

def contact(request):
    cart = Cart(request)

    
    context = {
       
        "contact_active":"active",
        'cart': cart
    }
    return render(request,"shop/contact.html",context)


def partners(request):
    cart = Cart(request)

    
    context = {
       
        "partners_active":"active",
        'cart': cart
    }
    return render(request,"shop/partners.html",context)

def pay(request):
    cart = Cart(request)

    
    context = {
       
        "ski":"active",
        'cart': cart
    }
    return render(request,"shop/pay.html",context)

def about(request):
    cart = Cart(request)

    
    context = {
       
        "about_active":"active",
        'cart': cart
    }
    return render(request,"shop/about.html",context)


    














































































































def adminCourses(request):
   
    context = {
       
        "adminCourses_active":"active",
       
    }
    return render(request,"shop/admin/manage-course.html",context)

def adminEarnings(request):
   
    context = {
       
        "adminEarnings_active":"active",
       
    }
    return render(request,"shop/admin/earnings.html",context)

def adminStatements(request):
   
    context = {
       
        "adminStatements_active":"active",
       
    }
    return render(request,"shop/admin/statements.html",context)

def adminAbout(request):
   
    context = {
       
        "adminWebinfo_active":"active",
       
    }
    return render(request,"shop/admin/about.html",context)

def adminPartners(request):
   
    context = {
       
        "adminWebinfo_active":"active",
       
    }
    return render(request,"shop/admin/partners.html",context)


def adminTalks(request):
   
    context = {
       
        "adminTalks_active":"active",
       
    }
    return render(request,"shop/admin/manage-talks.html",context)


def adminNews(request):
   
    context = {
       
        "adminNews_active":"active",
       
    }
    return render(request,"shop/admin/news.html",context)

def adminCourseNew(request):
   
    context = {
       
        "adminNeaaaaaaaaaaaaaaaaaws_active":"active",
       
    }
    return render(request,"shop/admin/new-course.html",context)

def adminCourseEdit(request):
   
    context = {
       
        "adminNaaaaaaaaaaaaaews_active":"active",
       
    }
    return render(request,"shop/admin/edit-course.html",context)


def adminTalkNew(request):
   
    context = {
       
        "adminNeaaaaaaaaaaaws_active":"active",
       
    }
    return render(request,"shop/admin/new-talk.html",context)

def adminTalkEdit(request):
   
    context = {
       
        "adminNaaaaaaaews_active":"active",
       
    }
    return render(request,"shop/admin/edit-talk.html",context)



    

    

    
