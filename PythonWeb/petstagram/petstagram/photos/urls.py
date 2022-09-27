from django.urls import path

from petstagram.photos.views import add_photo, show_photo_details, edit_photo

urlpatterns = (
    path('add/', add_photo, name='add-photo'),
    path('<int:pk>/', show_photo_details, name='show-photo-details'),
    path('<int:pk>/edit/', edit_photo, name='photo-edit'),

)
