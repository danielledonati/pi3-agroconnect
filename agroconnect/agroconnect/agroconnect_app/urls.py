from django.urls import path
from . import views
from .views import signup_view

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', signup_view, name='signup'),
]
