from django.urls import path
from .views import frstpg

urlpatterns = [
    path('',frstpg,name='frstpg')
]