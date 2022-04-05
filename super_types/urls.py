from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_types_list),
    path('api/super_type/', views.super_types_list),
    path('api/super_type/<int:pk>/', views.super_types_list),
]