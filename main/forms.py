from django import forms
from .models import Product, Version

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

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_current']

    def clean_is_current(self):
        cleaned_data = super().clean()
        is_current = cleaned_data.get('is_current')
        if is_current:
            active_count = self.instance.product.version_set.filter(is_current=True).exclude(
                id=self.instance.id).count()
            if active_count > 0:
                raise forms.ValidationError('Выберите только одну активную версию.')
        return is_current