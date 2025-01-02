from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def donate(request):
    return render(request, "donate.html")

def thank_you(request):
    return render(request, "thankyou.html")
