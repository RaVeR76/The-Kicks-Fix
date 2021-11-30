"""
This is a form which will be displayed in
Account section when user is super user, and utilised
to add and edit an Accessory without using admin page
"""
from django import forms
from common.models import Category, Colour
from .models import Accessories, Type


class AccessoriesForm(forms.ModelForm):
    """ Accessory form """
    class Meta:
        model = Accessories
        exclude = ('image1_url', 'image2_url', 'image3_url',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all().exclude(name='kicks')
        cat_friend_names = [(c.id, c.get_friendly_name()) for c in categories]

        type = Type.objects.all()
        type_friend_names = [(t.id, t.get_friendly_name()) for t in type]

        colour = Colour.objects.all()
        colour_friend_names = [(c.id, c.get_friendly_name()) for c in colour]

        self.fields['category'].choices = cat_friend_names
        self.fields['type'].choices = type_friend_names
        self.fields['colour'].choices = colour_friend_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
