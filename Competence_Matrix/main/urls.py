from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info', views.modelInfo, name='modelInfo'),
    path('add', views.modelInfo, name="modelAdd"),
    path('change', views.modelChange, name="modelChange")
]