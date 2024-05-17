from django.urls import path 
from apps.bbmodule import views

urlpatterns = [
    path('',views.index,name='index'),
    path('MakeUpList/',views.MakeUpList,name='MakeUpList'),
    path('HairList/',views.HairList,name='HairList'),
    path('PhotoList/',views.PhotoList,name='PhotoList'),
    path('Bridemaid/',views.Bridemaid,name='Bridemaid'),
    path('Home/',views.Home,name='Home'),
    path('search/',views.search,name='search'),
]
