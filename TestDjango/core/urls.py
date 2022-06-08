from django.urls import path
from .views import indexV3

urlpatterns =[
    path('',indexV3,name="home")

]
