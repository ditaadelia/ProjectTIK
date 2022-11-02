from django.forms import ModelForm
from django import forms
from tendik.models import Tendik

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
        }