from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .forms import GuestDetail,BusinessDetails,BookingForm

# Create your views here.
class BookWizardView(SessionWizardView):
    form_list = [GuestDetail,BusinessDetails,BookingForm]
    template_name = 'core/index.html'
    def done(self, form_list, **kwargs):
        return HttpResponse('form submitted')
