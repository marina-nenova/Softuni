from django.urls import path

from myMusicApp.album.views import add_album, album_details, edit_album, delete_album

urlpatterns = (
    path('add/', add_album, name='add-album'),
    path('details/<int:id>/', album_details, name='album-details'),
    path('edit/<int:id>/', edit_album, name='edit-album'),
    path('delete/<int:id>/', delete_album, name='delete-album'),
)