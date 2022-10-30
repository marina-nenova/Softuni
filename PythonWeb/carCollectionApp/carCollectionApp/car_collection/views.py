from django.shortcuts import render, redirect

from carCollectionApp.car_collection.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from carCollectionApp.car_collection.models import Profile, Car


def get_user_profile():
    return Profile.objects.first()


def get_car(pk):
    return Car.objects.get(pk=pk)


def get_all_cars():
    return Car.objects.all()


def show_index(request):
    user_profile = get_user_profile()
    context = {'user_profile': user_profile}
    return render(request, 'index.html', context)


def show_catalogue(request):
    cars = get_all_cars()
    context = {'cars': cars}
    return render(request, 'catalogue.html', context)


def create_car(request):
    form = CreateCarForm()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {'form': form}
    return render(request, 'car-create.html', context)


def show_car_details(request, pk):
    car = get_car(pk)
    context = {'car': car}
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = get_car(pk)
    form = EditCarForm(instance=car)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {'form': form}
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = get_car(pk)
    form = DeleteCarForm(instance=car)

    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {'form': form}
    return render(request, 'car-delete.html', context)


def create_profile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {'form': form}
    return render(request, 'profile-create.html', context)


def show_profile_details(request):
    user_profile = get_user_profile()

    if user_profile.first_name and user_profile.last_name:
        display_name = f'{user_profile.first_name} {user_profile.last_name}'
    elif user_profile.first_name:
        display_name = user_profile.first_name
    else:
        display_name = user_profile.last_name

    cars = get_all_cars()
    total_cars_price = sum([car.price for car in cars])
    context = {'user_profile': user_profile, 'display_name': display_name, 'total_cars_price': total_cars_price}
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    user_profile = get_user_profile()
    form = EditProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {'form': form}
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    user_profile = get_user_profile()
    cars = get_all_cars()
    form = DeleteProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            cars.delete()
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'profile-delete.html', context)
