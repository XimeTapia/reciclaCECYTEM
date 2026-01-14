from django import forms
#from django.forms import forms
from .models import Empleado



class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields=[
            'firts_name',
            'last_name',
            'job', 
            'departamento',
            'habilidades',
            'avatar'
        ]
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
