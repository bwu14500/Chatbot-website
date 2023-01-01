from django.urls import path 
from . import views

# URLConf
urlpatterns = [
    path('chat', views.chat),
    path('response', views.response)
]