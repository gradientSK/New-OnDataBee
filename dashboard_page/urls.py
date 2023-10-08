from django.urls import path
from . import views
#hello test git
urlpatterns = [
    path('dashboard/',views.dashboard_manager)

]