from django.urls import path

from myMusicApp.album.views import add_album, album_details, edit_album, delete_album

urlpatterns = (
    path('add/', add_album, name='add-album'),
    path('details/<str:pk>/', album_details, name='album-details'),
    path('edit/<str:pk>/', edit_album, name='edit-album'),
    path('delete/<str:pk>/', delete_album, name='delete-album'),
)