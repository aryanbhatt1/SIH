from .models import *
from django.forms import ModelForm


class AdmissionForm(ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
