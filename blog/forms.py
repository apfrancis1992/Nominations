from django import forms

from .models import Post, Nomination, Contracts

class PostForm(forms.ModelForm):

    class Meta:
        model = Nomination
        fields = ('contract', 'day_nom', 'day_nom_value', 'downstream_contract', 'downstream_ba', 'rank', 'author')


