
from django import forms

from item.models import Item



class FoundItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'status',
            'name',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
            'secret_information',
        ]