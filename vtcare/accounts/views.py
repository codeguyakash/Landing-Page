from django.shortcuts import render,redirect
from.models import *
from.forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
import random
from django.conf import settings



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            print(form.errors)  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request,'home.html')




def aboutus(request):
    return render(request,'aboutus.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home') 
            else:
                return render(request, 'login1.html', {'error': 'Your account is disabled.'})
        else:
            return render(request, 'login1.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login1.html')





def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contactus.html', {'form': form})

def send_otp(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Account.objects.filter(email=email).first()
            if user:
                otp = ''.join(random.choice('0123456789') for _ in range(6))  # Generate OTP
                request.session['otp'] = otp
                request.session['otp_email'] = email
                
                # Send OTP to user's email
                send_otp_email(email, otp)
                
                # Render OTP verification page
                return render(request, 'verify_otp.html', {'email': email})
            else:
                messages.error(request, 'Email not registered')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'forgot_password.html', {'form': form})

def send_otp_email(email, otp):
    subject = 'OTP for Password Reset'
    message = f'Your OTP for password reset is: {otp}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        email = request.POST.get('email')
        if otp_entered == stored_otp:
            request.session['reset_email'] = email
            return render(request, 'reset_password.html')
        else:
            messages.error(request, 'Invalid OTP')
    return redirect('send_otp')

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                email = request.session.get('reset_email')
                user = User.objects.filter(email=email).first()
                if user:
                    user.set_password(password)
                    user.save()
                    del request.session['otp']
                    del request.session['otp_email']
                    del request.session['reset_email']
                    messages.success(request, 'Password reset successful. You can now login with your new password.')
                    return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'forgot_password.html', {'form': form})

    
