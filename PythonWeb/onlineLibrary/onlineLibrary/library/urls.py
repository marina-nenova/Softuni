from django.urls import path

from onlineLibrary.library.views import show_index, add_book, edit_book, show_book_details, show_profile, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = (
    path('', show_index, name='show-index'),

    path('add/', add_book, name='add-book'),
    path('details/<int:pk>/', show_book_details, name='book-details'),
    path('edit/<int:pk>', edit_book, name='edit-book'),
    path('delete/<int:pk>/', delete_book, name='delete-book'),

    path('profile/create/', create_profile, name='create-profile'),
    path('profile/', show_profile, name='show-profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),
)
