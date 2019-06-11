from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="jc-home"),
        path('about/', views.about, name="jc-about"),
]
