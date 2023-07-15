from django.urls import path
from .views import indexx

urlpatterns = [
    path('', indexx)
]