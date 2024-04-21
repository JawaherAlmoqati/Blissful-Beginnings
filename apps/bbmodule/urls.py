from django.urls import path 
from apps.bbmodule import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bb', views.bb, name = "bb"),
    path('bb/<int:bId>', views.bb),
    path('filterbb', views.filterbb, name="filterbb")
   
]
