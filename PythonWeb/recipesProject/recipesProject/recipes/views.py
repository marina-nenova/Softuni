from django.shortcuts import render, redirect

from recipesProject.recipes.forms import CreateRecipeForm, DeleteRecipeForm
from recipesProject.recipes.models import Recipe


# Create your views here.

def show_index(request):
    recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def create_recipe(request):
    form = CreateRecipeForm()
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    form = CreateRecipeForm(instance=recipe)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    form = DeleteRecipeForm(instance=recipe)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'delete.html', context)


def show_recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    ingredients = [i for i in recipe.ingredients.split(', ')]

    context = {'recipe': recipe, 'ingredients': ingredients}
    return render(request, 'details.html', context)
