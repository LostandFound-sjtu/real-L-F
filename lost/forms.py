from django import forms
from item.models import Item
from tag.models import Tag

#  这里的这个人是没什么用处的


class LostItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'status',
            'name',
            'tag',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
            'secret_information',
        ]

class TagForm(forms.ModelForm):
    name=forms.CharField(max_length=128)
    slug=forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Tag
        fields=('name',)