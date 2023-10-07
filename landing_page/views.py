from django.shortcuts import render

# Create your views here.

def home_view (request):
    return render(request, 'landing_page/home_view.html')

def help_view (request):
    return render(request, 'landing_page/help_view.html')

def pricing_view (request):
    return render(request, 'landing_page/pricing_view.html')

def product_view (request):
    return render(request, 'landing_page/product_view.html')

def demo_view (request):
    return render(request, 'landing_page/demo_view.html')

def whoisitfor_view (request):
    return render(request, 'landing_page/whoisitfor_view.html')