from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('items/', views.items, name='items'),
    path('purchase/', views.purchase, name='purchase'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
]
