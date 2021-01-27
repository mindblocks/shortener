from django.conf import settings
from django.urls import path, include
from .views import redirector

urlpatterns = [
    path('', redirector),
]

