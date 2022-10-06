from django.forms import ModelForm

from myMusicApp.album.models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
