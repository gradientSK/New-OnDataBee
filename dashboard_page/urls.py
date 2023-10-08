from django.urls import path
from . import views
#hello test git

urlpatterns = [
    path('dashboard/', views.dashboard_view),
    path('dashboardmanager/', views.dashboardmanager_view),
    path('integrations/', views.integrations_view),
    path('export/', views.export_view),
    path('savedtmp/', views.savedtemplates_view),
    path('whitelabel/', views.whitelabel_view),
    path('logomanager/', views.logomanager_view),
]