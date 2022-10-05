from django.contrib import admin
from django.urls import path, include

from myMusicApp.album.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('album/', include('myMusicApp.album.urls')),
    path('profile/', include('myMusicApp.user_profile.urls'))
]
