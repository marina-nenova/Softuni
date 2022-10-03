from django.urls import path

from petstagram.common.views import home, like_functionality, copy_link_to_clipboard

urlpatterns = (
    path('', home, name='home'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),

)
