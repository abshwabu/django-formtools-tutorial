from django import forms
from .models import Guest,Business,Booking

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
        fields = ('name',)



class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields =('room_type', 'date','number_of_nights')
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
