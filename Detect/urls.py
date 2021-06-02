from django.urls import path, include
from . import views

print('ULRS')
urlpatterns = [
    path('', views.index, name='detect')
]