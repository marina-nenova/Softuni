from django.urls import path

from notesApp.notes.views import show_index, add_note, edit_note, delete_note, show_note_details, show_profile \
    , create_profile, delete_profile

urlpatterns = (
    path('', show_index, name='home'),
    path('add/', add_note, name='add-note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete-note'),
    path('details/<int:pk>/', show_note_details, name='note-details'),
    path('profile/', show_profile, name='show-profile'),
    path('profile/register', create_profile, name='create-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),
)
