from django.shortcuts import render, resolve_url, redirect
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def home(request):
    all_photos = Photo.objects.all()

    context = {'all_photos': all_photos}
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    # photo_like = Like(id=photo_id)
    # photo_like.save()

    # Like.objects.create(id=photo_id)

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('show-photo-details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
