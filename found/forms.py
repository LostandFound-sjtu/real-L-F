
from django import forms

from item.models import Item
from tag.models import Tag


class FoundItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'tag',
            'mail_address',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
        ]

#  tag类里面是有自动填充功能的emm
class TagForm(forms.ModelForm):
    name=forms.CharField(max_length=128)
    #slug=forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Tag
        fields=('name',)
