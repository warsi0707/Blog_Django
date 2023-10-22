from django.forms import ModelForm
from .models import contactUs

class contactForm(ModelForm):
    class Meta:
        model = contactUs
        fields = '__all__'