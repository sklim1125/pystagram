#coding: utf-8

from django import forms
from photo.models import Photo

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description',)

# if inherit from Form class, this form class  could be defind at below.
#class PhotoEditForm(forms.Form):
#    image_file = forms.ImageField()
#    filtered_image = forms.ImageField()
#    description = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
#    created_at = forms.DateTimeField(required=False)
