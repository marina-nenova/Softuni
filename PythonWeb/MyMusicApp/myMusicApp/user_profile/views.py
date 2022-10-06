from django.shortcuts import render

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
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
    else:
        albums = Album.objects.all()
        context = {'albums': albums }
        return render(request, 'home-with-profile.html', context)


def profile_details(request):

    return render(request, 'user_profile/profile-details.html')


def profile_delete(request):

    return render(request, 'user_profile/profile-delete.html')
