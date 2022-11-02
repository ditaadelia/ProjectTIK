from django.forms import ModelForm
from django import forms
from mahasiswa.models import Mahasiswa

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'nim' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'ttl' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
        }