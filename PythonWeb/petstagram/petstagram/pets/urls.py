from django.urls import path

from petstagram.pets.views import add_pet, show_pet_details, edit_pet, delete_pet

urlpatterns = (
    path('add/', add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', show_pet_details, name='pet-details'),
    path('<str:username>/pet/<slug:pet_name>/edit/', edit_pet, name='pet-edit'),
    path('<str:username>/pet/<slug:pet_name>/delete/', delete_pet, name='pet-delete'),

)
