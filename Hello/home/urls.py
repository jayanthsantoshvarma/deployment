from django.contrib import admin
from django.urls import path
from home import views
from .views import home, result

urlpatterns = [
    path('', views.index, name="home"),
    path("handwritten_digit_recognition_model/", views.hdr, name="handwritten_digit_recognition"),
    path('titanic_survival_predictor/', views.home, name='titanic_home'),
    path('titanic_survival_predictor/result/', views.result, name='result')
]