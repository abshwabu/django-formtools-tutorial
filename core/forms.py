from django import forms
from .models import Guest

class GuestDetail(forms.ModelForm):
    Bool_options = [{True: 'Yes', False: 'No'}]
    is_business = forms.BooleanField(
        widget= forms.RadioSelect(choices=Bool_options, default=False,required=False)
    )
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email','phone' )
