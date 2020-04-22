from django import forms
from person.models import Person
from item.models import Item
from tag.models import Tag

#  这里的这个人是没什么用处的
class LostPersonModelForm(forms.ModelForm):
    class Meta:
        model = Person

        fields = [
            'status',
            'person',
            'name',
            'father_name',
            'mother_name',
            'gender',
            'age',
            'body_color',
            'height',
            'image',
            'phone_number',
            'identification_mark',
            'secret_information'
        ]


class LostItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'status',
            'name',
            'tags',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
            'secret_information',
        ]

