from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('contactus/',views.contactus,name='contactus'),
    path('forgot_password/',views.forgot_password,name="forgot_password")
    
    
]