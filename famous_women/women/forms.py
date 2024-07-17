from django import forms
from women.models import Women


class WomenForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ('title', 'content')
