"""
This is a form which will be displayed in
Account section when user is super user, and utilised
to add and edit Kicks without using admin page
"""
from django import forms
from common.models import Category, Sex, Colour
from .models import Kicks, Brand, Style


class KicksForm(forms.ModelForm):
    """ Kicks form """
    class Meta:
        model = Kicks
        exclude = ('image1_url', 'image2_url', 'image3_url',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all().exclude(name='accessories')
        cat_friend_names = [(c.id, c.get_friendly_name()) for c in categories]

        sex = Sex.objects.all()
        sex_friend_names = [(s.id, s.get_friendly_name()) for s in sex]

        brand = Brand.objects.all()
        brand_friend_names = [(b.id, b.get_friendly_name()) for b in brand]

        style = Style.objects.all()
        style_friend_names = [(s.id, s.get_friendly_name()) for s in style]

        colour = Colour.objects.all()
        colour_friend_names = [(c.id, c.get_friendly_name()) for c in colour]

        self.fields['category'].choices = cat_friend_names
        self.fields['sex'].choices = sex_friend_names
        self.fields['brand'].choices = brand_friend_names
        self.fields['style'].choices = style_friend_names
        self.fields['colour'].choices = colour_friend_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
