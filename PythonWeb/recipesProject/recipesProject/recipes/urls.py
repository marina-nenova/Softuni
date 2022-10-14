from django.urls import path

from recipesProject.recipes.views import show_index, create_recipe, edit_recipe, delete_recipe, show_recipe_details

urlpatterns = (
    path('', show_index, name='home'),
    path('create/', create_recipe, name='create-recipe'),
    path('edit/<int:id>/', edit_recipe, name='edit-recipe'),
    path('delete/<int:id>/', delete_recipe, name='delete-recipe'),
    path('details/<int:id>/', show_recipe_details, name='recipe-details'),
)
