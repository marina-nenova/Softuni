from django.forms import ModelForm

from myMusicApp.album.models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
