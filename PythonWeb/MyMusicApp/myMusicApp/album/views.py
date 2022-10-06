from django.shortcuts import render, redirect

from myMusicApp.album.forms import AlbumForm
from myMusicApp.album.models import Album


def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(id=pk)

    context = {'album': album}
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    return render(request, 'album/edit-album.html')


def delete_album(request, pk):
    return render(request, 'album/delete-album.html')
