from django.urls import path

from myMusicApp.user_profile.views import profile_details, profile_delete

urlpatterns = (
    path('details/', profile_details, name='profile-details'),
    path('delete/', profile_delete, name='profile-delete'),

)