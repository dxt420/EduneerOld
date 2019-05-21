
from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    
    
    path('', views.home , name="home"),
    path('courses', views.courses , name="courses"),
    path('mycourses', views.mycourses , name="mycourses"),
    path('coursedetail', views.coursedetail , name="coursedetail"),
    path('talks', views.talks , name="talks"),
    path('talkdetail', views.talkdetail , name="talkdetail"),
    path('cart', views.cart , name="cart"),
    path('news', views.news , name="news"),
    path('contact', views.contact , name="contact"),
    path('partners', views.partners , name="partners"),
    path('pay', views.pay , name="pay"),
    path('about', views.about , name="about"),
    path('register', views.register , name="register"),
    path('completeregister', views.completeregister , name="completeregister"),
    path('login', views.login , name="login"),
    path('logout', views.logout , name="logout"),
    path('forgot', views.forgot , name="forgot"),
    
    
]
