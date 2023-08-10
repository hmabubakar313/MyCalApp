from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('breakfast/', views.BreakfastViewSet.as_view()),
    path('lunch/', views.LunchViewSet.as_view()),
    path('dinner/', views.DinnerViewSet.as_view()),
]
