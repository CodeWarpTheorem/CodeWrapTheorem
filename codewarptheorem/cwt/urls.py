from django.urls import include, path
from cwt import views 

urlpatterns = [
    path('',views.home),

]