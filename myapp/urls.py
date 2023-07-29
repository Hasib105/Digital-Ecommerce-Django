from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('success/', views.payment_success_view, name = 'success'),
    path('failed/', views.payment_failed_view, name = 'failed'),
    path('product/<int:pk>', views.detail, name = 'detail'),
    path('api/checkout-session/<int:pk>', views.create_checkout_session, name = 'api_checkout_session'),
    path('createproduct/', views.create_product, name = 'createproduct'),
    path('editproduct/<int:pk>', views.product_edit, name = 'editproduct'),
    path('deleteproduct/<int:pk>', views.product_delete, name = 'deleteproduct'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('invalid/',views.invalid,name='invalid'),
]
 