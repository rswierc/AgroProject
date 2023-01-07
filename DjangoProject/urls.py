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
    #main page urls
    path('', MainPageView.weather),
    #cow urls
    path('cow/table/', CowView.tableCow),
    path('cow/create/', CowView.createCow, name="create"),
    path('cow/update/<str:pk>', CowView.updateCow, name="update"),
    path('cow/delete/<str:pk>', CowView.deleteCow, name="delete"),
    path('cow/note/<str:pk>', CowView.noteCow, name="note"),
    path('cow/search', CowView.searchEaringNum, name="cow/search"),
    path('cow/sort/birth', CowView.sortCow_birth, name="sort_birth_date"),
    path('cow/sort/sale', CowView.sortCow_sale, name="sort_birth_sale"),
    path('cow/sort/sex', CowView.sortCow_sex, name="sort_birth_sex"),

    #sheep urls
    path('sheep/table/', SheepView.tableSheep),
    path('sheep/create/', SheepView.createSheep, name="create"),
    path('sheep/update/<str:pk>', SheepView.updateSheep, name="update"),
    path('sheep/delete/<str:pk>', SheepView.deleteSheep, name="delete"),
    path('sheep/note/<str:pk>', SheepView.noteSheep, name="note"),
    path('sheep/search', SheepView.searchEaringNum, name="sheep/search"),
    path('sheep/sort/birth', SheepView.sortSheep_birth, name="sort_birth_date"),
    path('sheep/sort/sale', SheepView.sortSheep_sale, name="sort_birth_sale"),
    path('sheep/sort/sex', SheepView.sortSheep_sex, name="sort_birth_sex"),
]
