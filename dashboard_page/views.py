from django.shortcuts import render
import requests
from .forms import id_field
from .models import youtube_id
# Create your views here.
def dashboardmanager_view (request):
    return render(request, 'dashboard_page/dashboardmanager_view.html')

def dashboard_view (request):
    form = id_field(request.POST or None)
    if form.is_valid():
        form.save()
        form = id_field()
    obj = youtube_id.objects.latest('id')
    response= requests.get('https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id='+obj.channelid+'&key=AIzaSyB05OHI0VW8o9ulDYogfJo0Q5S6qJfgxmU')
    return render(request, 'dashboard_page/dashboard_view.html', {'form': form ,'response': response})

def integrations_view (request):
    return render(request, 'dashboard_page/integrations_view.html')

def export_view (request):
    return render(request, 'dashboard_page/export_view.html')

def savedtemplates_view (request):
    return render(request, 'dashboard_page/savedtemplates_view.html')

def whitelabel_view (request):
    return render(request, 'dashboard_page/whitelabel_view.html')

def logomanager_view (request):
    return render(request, 'dashboard_page/logomanager_view.html')

# UCA862HkLaGzmZ32j2m3lUKg