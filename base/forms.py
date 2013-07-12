from django import forms


class NewsSubscribeForm(forms.Form):

    email = forms.EmailField(required=True)
