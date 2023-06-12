from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = ['радар', 'криптоферма', 'майнинг', 'оружие']
        for word in forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError("Недопустимое слово в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = ['радар', 'криптоферма', 'майнинг', 'оружие']
        for word in forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError("Недопустимое слово в описании продукта.")
        return description