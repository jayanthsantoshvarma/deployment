from django.contrib import admin
from django.urls import path

from .views import home, result

urlpatterns = [
    path('titanic_survival_predictor/', home, name='home'),
    path('titanic_survival_predictor/result/', result, name='result')
]