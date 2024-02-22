from django.urls import path ,include
from apps.bbmodule import views

urlpatterns = [
    path('',views.index,name='index'),
]
