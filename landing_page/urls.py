from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('demo/',views.demo_view),
    path('help/',views.help_view),
    path('pricing/',views.pricing_view),
    path('product/',views.product_view),
    path('usecase/',views.usecase_view),
]