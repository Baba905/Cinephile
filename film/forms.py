from django import forms


class Search(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": " Search"
        }
    ))
