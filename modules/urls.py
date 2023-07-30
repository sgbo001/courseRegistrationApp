from django.urls import path
from . import views
from .views import module_detail, my_module


app_name = 'modules'
urlpatterns = [
    path('', views.course_list, name='home'),
    path('modules/', views.module_list, name='module_list'),
    path('module_detail/', module_detail, name='module_detail'),
    path('unregister_module/<str:module_code>/', views.unregister_module, name='unregister_module'),
    path('register_module/<str:module_code>/', views.register_module, name='register_module'),
    path('my_module/', my_module, name='my_module'),

]