from django.urls import include, path
from .views import home

urlpatterns = [
    path('/',views.home(),name="home" ),

]