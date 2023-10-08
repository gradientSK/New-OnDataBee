from django.shortcuts import render

# Create your views here.
def dashboardmanager_view (request):
    return render(request, 'dashboard_page/dashboardmanager_view.html')

def dashboard_view (request):
    return render(request, 'dashboard_page/dashboard_view.html')

def integrations_view (request):
    return render(request, 'dashboard_page/integrations_view.html')

def export_view (request):
    return render(request, 'dashboard_page/export_view.html')

def savedtemplates_view (request):
    return render(request, 'dashboard_page/savedtemplates.html')

def whitelabel_view (request):
    return render(request, 'dashboard_page/whitelabel_view.html')

def logomanager_view (request):
    return render(request, 'dashboard_page/logomanager.html')
