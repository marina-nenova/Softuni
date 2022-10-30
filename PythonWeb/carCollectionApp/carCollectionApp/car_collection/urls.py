from django.urls import path

from carCollectionApp.car_collection.views import show_index, create_profile, show_catalogue, create_car, \
    show_car_details, edit_car, delete_car, show_profile_details, edit_profile, delete_profile

urlpatterns = (
    path('', show_index, name='home'),
    path('profile/create/', create_profile, name='create profile'),
    path('catalogue/', show_catalogue, name='show catalogue'),
    path('car/create/', create_car, name='create car'),
    path('car/<int:pk>/details/', show_car_details, name='car details'),
    path('car/<int:pk>/edit/', edit_car, name='edit car'),
    path('car/<int:pk>/delete/', delete_car, name='delete car'),
    path('profile/details/', show_profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)
