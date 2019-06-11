"""shop_mngr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Using the include function will chop off what django has matched.
# Evertything after the match is sent to the destination.
#
# matched 'jc/something'
# 'something' is sent to job_card/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jc/', include('job_cards.urls')),
]
