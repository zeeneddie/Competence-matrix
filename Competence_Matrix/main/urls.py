from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('info', views.ShowModelsInfo, name='modelInfo'),
    path('add', views.AddModel, name="modelAdd"),
    path('change', views.ChangeModel, name="modelChange"),
    path('delete', views.DeleteModel, name="modelDelete")
]