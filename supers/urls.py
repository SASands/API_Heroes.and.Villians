from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('custom/', views.super_types_list),
    path('api/supers/<int:pk>/', views.supers_detail),
]