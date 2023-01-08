from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Cows import views as CowView
from MainPage import views as MainPageView
from Sheep import views as SheepView
from Field import views as FieldView

urlpatterns = [
    path('admin/', admin.site.urls),
    #main page urls
    path('', MainPageView.weather),
    #cow urls
    path('cow/table/', CowView.tableCow),
    path('cow/create/', CowView.createCow, name="create_cow"),
    path('cow/update/<str:pk>', CowView.updateCow, name="update_cow"),
    path('cow/delete/<str:pk>', CowView.deleteCow, name="delete_cow"),
    path('cow/note/<str:pk>', CowView.noteCow, name="note_cow"),
    path('cow/search', CowView.searchEaringNum, name="cow/search"),
    path('cow/sort/birth', CowView.sortCow_birth, name="sort_birth_date"),
    path('cow/sort/sale', CowView.sortCow_sale, name="sort_birth_sale"),
    path('cow/sort/sex', CowView.sortCow_sex, name="sort_birth_sex"),

    #sheep urls
    path('sheep/table/', SheepView.tableSheep),
    path('sheep/create/', SheepView.createSheep, name="create_sheep"),
    path('sheep/update/<str:pk>', SheepView.updateSheep, name="update_sheep"),
    path('sheep/delete/<str:pk>', SheepView.deleteSheep, name="delete_sheep"),
    path('sheep/note/<str:pk>', SheepView.noteSheep, name="note_sheep"),
    path('sheep/search', SheepView.searchEaringNum, name="sheep/search"),
    path('sheep/sort/birth', SheepView.sortSheep_birth, name="sort_birth_date"),
    path('sheep/sort/sale', SheepView.sortSheep_sale, name="sort_birth_sale"),
    path('sheep/sort/sex', SheepView.sortSheep_sex, name="sort_birth_sex"),

    #field urls
    path('field/table/', FieldView.tableField),
    path('field/create/', FieldView.createField, name="create_field"),
    path('field/update/<str:pk>', FieldView.updateField, name="update_field"),
    path('field/delete/<str:pk>', FieldView.deleteField, name="delete_field"),
    path('field/treatment/<str:pk>', FieldView.treatmentField, name="treatment_field"),
    path('field/treatment/<str:pk>', FieldView.treatmentField, name="treatment_field"),
    path('field/treatment/spraying/<str:pk>', FieldView.sprayingField, name="spraying_field"),
    path('field/treatment/fertilization/<str:pk>', FieldView.fertilizationField, name="fertilization_field"),
    path('field/treatment/harvest/<str:pk>', FieldView.harvestField, name="harvest_field"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
