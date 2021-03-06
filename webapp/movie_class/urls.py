from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dataset', views.exploreDataset, name="dataset"),
    path('result', views.result, name="result")
]