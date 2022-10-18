from django.shortcuts import render, redirect

from gamesPlayApp.game.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from gamesPlayApp.game.models import Profile, Game


def get_user_profile():
    return Profile.objects.first()


def show_index(request):
    user_profile = get_user_profile()
    context = {'user_profile': user_profile}
    return render(request, 'home-page.html', context)


def create_profile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create-profile.html', context)


def show_dashboard(request):
    user_profile = get_user_profile()
    games = Game.objects.all()
    context = {'games': games, 'user_profile': user_profile}
    return render(request, 'dashboard.html', context)


def create_game(request):
    user_profile = get_user_profile()
    form = CreateGameForm()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'create-game.html', context)


def show_game_details(request, pk):
    user_profile = get_user_profile()
    game = Game.objects.get(pk=pk)

    context = {'game': game, 'user_profile': user_profile}
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    user_profile = get_user_profile()
    game = Game.objects.get(pk=pk)
    form = EditGameForm(instance=game)
    if request.method == 'POST':
        form = CreateGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    user_profile = get_user_profile()
    game = Game.objects.get(pk=pk)
    form = DeleteGameForm(instance=game)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'delete-game.html', context)


def show_profile_details(request):
    user_profile = get_user_profile()
    games = Game.objects.all()
    if user_profile.first_name and user_profile.last_name:
        display_name = f'{user_profile.first_name} {user_profile.last_name}'
    elif user_profile.first_name:
        display_name = user_profile.first_name
    else:
        display_name = user_profile.last_name
    try:
        average_games_rating = sum([g.rating for g in games]) / games.count()
    except ZeroDivisionError:
        average_games_rating = 0

    context = {'user_profile': user_profile, 'display_name': display_name, 'games': games,
               'average_games_rating': average_games_rating}
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    user_profile = get_user_profile()
    form = EditProfileForm(instance=user_profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user_profile = get_user_profile()
    games = Game.objects.all()
    form = DeleteProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            games.delete()
            form.save()
            return redirect('home')

    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'delete-profile.html', context)
