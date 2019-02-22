from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('banking/', views.banking, name='banking'),
    path('chatacc/', views.chatacc, name='chatacc'),
    path('manual/', views.manual, name='manual'),
    path('currency/', views.currency, name='currency'),
    path('translocking/', views.translocking, name='translocking'),
    path('items/', views.items, name='items'),
    path('purchase/', views.purchase, name='purchase'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('creditnotes/', views.creditnotes, name='creditnotes'),
    path('deliverychallans/', views.deliverychallans, name='deliverychallans'),
    path('estimates/', views.estimates, name='estimates'),
    path('invoices/', views.invoices, name='invoices'),
    path('paymentrecevied/', views.paymentrecevied, name='paymentrecevied'),
    path('recurringinvoices/', views.recurringinvoices, name='recurringinvoices'),
    path('retainerinvoice/', views.retainerinvoice, name='retainerinvoice'),
    path('salesorders/', views.salesorders, name='salesorders'),
]
