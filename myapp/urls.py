from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('success/', views.payment_success_view, name = 'success'),
    path('failed/', views.payment_failed_view, name = 'failed'),
    path('product/<int:pk>', views.detail, name = 'detail'),
    path('api/checkout-session/<int:pk>', views.create_checkout_session, name = 'api_checkout_session'),
]
 