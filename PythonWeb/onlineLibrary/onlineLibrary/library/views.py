from django.shortcuts import render, redirect

from onlineLibrary.library.forms import BookForm, ProfileForm, EditBookForm, EditProfileForm, DeleteProfileForm
from onlineLibrary.library.models import Profile, Book


def show_index(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    if not profile:
        return redirect('create-profile')

    context = {
        'profile': profile,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = Profile.objects.first()
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-index')

    context = {'form': form, 'profile': profile, }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    form = EditBookForm(instance=book)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show-index')

    context = {'form': form, 'book': book, 'profile': profile}
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('show-index')


def show_book_details(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)

    context = {'book': book, 'profile': profile, }
    return render(request, 'book-details.html', context)


def create_profile(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-index')

    context = {'form': form}
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()

    context = {'profile': profile}
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show-profile')

    context = {'form': form, 'profile': profile, }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    books = Book.objects.all()
    profile = Profile.objects.first()

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        books.delete()
        form.save()
        return redirect('show-index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {'form': form, 'profile': profile, }
    return render(request, 'delete-profile.html', context)
