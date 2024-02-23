from django.urls import path ,include
from apps.bbmodule import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bb',views.bb),
    path('bb1/<int:bID>', views.bb1)
]
