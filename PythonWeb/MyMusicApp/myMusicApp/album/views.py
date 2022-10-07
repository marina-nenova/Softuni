from django.shortcuts import render, redirect

from myMusicApp.album.forms import AlbumForm, DeleteAlbumForm
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
    album = Album.objects.get(id=pk)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home')

    context = {'form': form}
    return render(request, 'album/delete-album.html', context)
