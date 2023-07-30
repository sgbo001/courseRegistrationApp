from django.urls import path
from . import views
from .views import password_reset_view


app_name = 'users'
urlpatterns = [
    path('password-reset/', password_reset_view, name='password_reset'),
]