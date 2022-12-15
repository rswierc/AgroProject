"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Cows import views as CowView
from MainPage import views as MainPageView
from Sheep import views as SheepView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.main),
    path('cow/table/', CowView.cows_table),
    path('cow/create/', CowView.get_cow),
    path('cow/new/', CowView.createCow),
    path('cow/update/<str:pk>', CowView.updateCow, name="update"),
    path('cow/delete/<str:pk>', CowView.deleteCow, name="delete"),
    path('cow/sort', CowView.sortEaringNum , name="sort"),

]
