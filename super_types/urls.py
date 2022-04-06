from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_types_list),
    path('api/super_types/', views.super_types_list),
    path('api/super_types/<int:fk>/', views.super_types_detail),
]