from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .forms import GuestDetail,BusinessDetails,BookingForm

# Create your views here.
def show_business_details(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('is_business')
class BookWizardView(SessionWizardView):
    form_list = [GuestDetail,BusinessDetails,BookingForm]
    template_name = 'core/index.html'
    condition_dict = {'1': show_business_details}
    def done(self, form_list, **kwargs):
        guest_form = form_list[0]
        business_form = form_list[1]

        if guest_form.cleaned_data.get('is_business'):
            business = business_form.save()
            guest = guest_form.save(commit=False)
            guest.business = business
            guest.save()
        else:
            guest = guest_form.save()

        # Use the correct variable name: guest, not gust
        booking_form = form_list[-1]
        booking = booking_form.save(commit=False)

        # Check if guest is defined before accessing it
        if 'guest' in locals():
            booking.guest = guest
            booking.save()
            return HttpResponse('Form submitted')
        else:
            # Print information for debugging
            print("Guest not defined!")
            print("guest_form.cleaned_data:", guest_form.cleaned_data)
            print("business_form.cleaned_data:", business_form.cleaned_data)

        # Return an error response or redirect as needed
        return HttpResponse('Error in form submission')
