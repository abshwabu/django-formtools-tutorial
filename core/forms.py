from django import forms
from .models import Guest,Business

class GuestDetail(forms.ModelForm):
    Bool_options = [{True, 'Yes'}, {False, 'No'}]
    is_business = forms.BooleanField(
        widget= forms.RadioSelect(choices=Bool_options),required=False
    )
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email','phone' )


class BusinessDetails(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = ('name')
