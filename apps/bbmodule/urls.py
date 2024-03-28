from django.urls import path 
from apps.bbmodule import views

urlpatterns = [
    path('',views.index,name='index')
   
]
