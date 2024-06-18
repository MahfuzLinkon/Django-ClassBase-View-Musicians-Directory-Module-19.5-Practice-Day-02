from django import forms
from . import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        exclude = ['release_date']