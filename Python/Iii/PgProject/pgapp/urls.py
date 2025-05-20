from django.urls import path
from .views import HiPgView,AboutView
urlpatterns = [
    path('',HiPgView.as_view(),name='hi'),
    path('about/',AboutView.as_view(),name='iii'),
]