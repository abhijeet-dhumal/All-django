from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request,'covicare_home.html')

def chat(request):
    return render(request,'covicare_chat.html')

def covicare_about(request):
    return render(request,'covicare_about.html')

def contact(request):
    return render(request,'covicare_contact.html')
