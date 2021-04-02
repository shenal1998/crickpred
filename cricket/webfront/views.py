from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import views
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages, auth

# from . import json
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

    
        # body={
        #     'First Name': request.POST['first_name'],
        #     'phone': request.POST['last_name'],
        #     'email': request.POST['email'],
        #     'Phone': request.POST['phone'],
        #     'message': request.POST['message'],
        #   }
      
        #sending the email
        send_mail(
            first_name,  # firstname
            email,  # fromemail
            message,  # message
            ['shenal1998@gmail.com'],  # To Email
        )

        messages.success(
            request, 'Thank you Message Send Succesfully we will Contact you soon')
        return render(request, 'contact.html', {'first_name': first_name})

    else:
        return render(request, 'contact.html', {})





