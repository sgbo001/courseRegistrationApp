from django.urls import path
from . import views
from .views import module_detail

app_name = 'modules'
urlpatterns = [
    path('', views.course_list, name='home'),
    path('modules/', views.module_list, name='module_list'),
    path('module_detail/', module_detail, name='module_detail'),

]