from django import forms

from recipesProject.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Recipe name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Url to recipe image'}),
            'description': forms.TextInput(attrs={'placeholder': 'How to prepare'}),
            'ingredients': forms.TextInput(attrs={'placeholder': 'e.g: 2 eggs, 500ml milk, 2tbsp oil, ...'}),
            'time': forms.NumberInput(attrs={'placeholder': 'Time to prepare in minutes'}),
        }


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            # field.widget.attrs['required'] = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
