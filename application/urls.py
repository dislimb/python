from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('passcode', views.passcode),
    path('dash', views.dash),
    path('snake', views.snake),
    path('hardsnake', views.hardsnake)
]