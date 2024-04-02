from django.urls import path
from agroconnect_app import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('admin/', admin.site.urls)
]
