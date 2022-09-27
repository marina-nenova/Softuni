from django.urls import path

from petstagram.common.views import home

urlpatterns = (
    path('', home, name='home'),

)
