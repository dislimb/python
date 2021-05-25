from django.urls import path
from . import views


urlpatterns = [
    path('hard/', views.index),
    path('hard/passcode', views.passcode),
    path('hard/dash', views.dash),
    path('hard/snake', views.snake),
]