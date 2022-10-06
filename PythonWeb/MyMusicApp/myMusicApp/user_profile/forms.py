from django.forms import ModelForm, models

from myMusicApp.user_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
