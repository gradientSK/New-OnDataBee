from django.shortcuts import render

# Create your views here.
def dashboard_manager (request):
    return render(request, 'dashboard_page/dashboard_manager.html')