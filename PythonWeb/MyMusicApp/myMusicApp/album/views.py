from django.shortcuts import render


def home(request):
    return render(request, 'home-no-profile.html')


def add_album(request):
    return render(request, 'album/add-album.html')


def album_details(request, pk):
    return render(request, 'album/album-details.html')


def edit_album(request, pk):
    return render(request, 'album/edit-album.html')


def delete_album(request, pk):
    return render(request, 'album/delete-album.html')
