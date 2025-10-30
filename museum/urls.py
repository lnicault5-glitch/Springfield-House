from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visit/', views.visit, name='visit'),
    path('history/', views.history, name='history'),
    path('art/', views.art, name='art'),
    path('archbold/', views.archbold, name='archbold'),
    path('springfieldforward/', views.springfieldforward, name='springfieldforward'),
    path('contact/', views.contact, name='contact'),
]