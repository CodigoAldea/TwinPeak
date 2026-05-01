from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def how_we_work(request):
    return render(request, 'howwework.html')

def insights(request):
    return render(request, 'insights.html')

def about_us(request):
    return render(request, 'aboutus.html')

def work_with_us(request):  
    return render(request, 'workwithus.html')