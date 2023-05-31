from django.forms import ModelForm
from .models import Dusting

class DustingForm(ModelForm):
  class Meta:
    model = Dusting
    fields = ['date', 'dust']