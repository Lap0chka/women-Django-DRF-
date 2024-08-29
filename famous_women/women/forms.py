from django import forms

from women.models import Women, Categories


class WomenForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label='No categories', required=False)

    class Meta:
        model = Women
        fields = ('title', 'content', 'image', 'cat')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 35, 'cols': 60}),
        }
