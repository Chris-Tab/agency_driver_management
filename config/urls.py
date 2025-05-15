"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from accounts import views as accounts_views
from shifts import views as shifts_views


urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('admin/', admin.site.urls),

    # Company Signup
    path('signup/', accounts_views.company_signup, name='company_signup'),

    # Login and Logout
    path('login/', accounts_views.custom_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', accounts_views.company_dashboard, name='company_dashboard'),
    path('shift/create/', shifts_views.shift_create, name='shift_create'),
    path('driver/dashboard/', accounts_views.driver_dashboard, name='driver_dashboard'),
    path('shift/<int:pk>/view/', shifts_views.shift_view, name='shift_view'),
    path('shift/<int:pk>/edit/', shifts_views.shift_edit, name='shift_edit'),
    path('shift/<int:pk>/delete/', shifts_views.shift_delete, name='shift_delete'),
    path('driver/holidays/', shifts_views.holiday_request, name='holiday_request'),


    

]
