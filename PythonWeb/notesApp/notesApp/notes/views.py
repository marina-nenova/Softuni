from django.shortcuts import render, redirect

from notesApp.notes.forms import CreateProfileForm, CreateNoteForm, DeleteNoteForm
from notesApp.notes.models import Profile, Note


def show_index(request):
    user_profile = Profile.objects.first()
    notes = Note.objects.all()
    if not user_profile:
        return redirect('create-profile')

    context = {'user_profile': user_profile, 'notes': notes}
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    user_profile = Profile.objects.first()
    form = CreateNoteForm()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    form = CreateNoteForm(instance=note)
    user_profile = Profile.objects.first()

    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    user_profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    form = DeleteNoteForm(instance=note)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        form.save()
        return redirect('home')

    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'note-delete.html', context)


def show_note_details(request, pk):
    user_profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    context = {'note':note, 'user_profile': user_profile}
    return render(request, 'note-details.html', context)


def create_profile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'home-no-profile.html', context)



def show_profile(request):
    user_profile = Profile.objects.first()
    all_notes = Note.objects.all().count()

    context = {'user_profile': user_profile, 'all_notes': all_notes}
    return render(request, 'profile.html', context)


def delete_profile(request):
    user_profile = Profile.objects.first()
    all_notes = Note.objects.all()

    user_profile.delete()
    all_notes.delete()
    return redirect('home')

