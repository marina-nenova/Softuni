from django.shortcuts import render, redirect

from myMusicApp.album.models import Album
from myMusicApp.user_profile.forms import ProfileForm
from myMusicApp.user_profile.models import Profile


def home(request):
    user = Profile.objects.first()
    if not user:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home-with-profile.html')
        context = {'user': user, 'form': form}
        return render(request, 'home-no-profile.html', context)
    else:
        albums = Album.objects.all()
        context = {'albums': albums }
        return render(request, 'home-with-profile.html', context)


def profile_details(request):
    user = Profile.objects.first()
    all_albums = len(Album.objects.all())
    context = {'user': user, 'all_albums': all_albums}
    return render(request, 'user_profile/profile-details.html', context)


def profile_delete(request):
    albums = Album.objects.all()
    profile = Profile.objects.first()
    if request.method == "POST":
        profile.delete()
        albums.delete()
        return redirect('home')
    return render(request, 'user_profile/profile-delete.html')
