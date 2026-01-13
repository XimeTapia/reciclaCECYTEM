#from django.shortcuts import render
from django.views.generic.edit import FormView

from.models import Departamento
from applications.personas.models import Empleado
from .forms import NewDepartamentoForm

from django.views.generic import (ListView)

class DepartamentoListView(ListView):
    model=Departamento
    template_name="departamento/lista.html"
    context_object_name='departamentos'

class NewDepartamentoView(FormView):
    
    template_name='departamento/new_departamento.html'
    form_class=NewDepartamentoForm
    success_url='/'

    def form_valid(self, form):

        #crear un departamento
        depa=Departamento(
            nombre=form.cleaned_data['departamento'],  
            subnombre=form.cleaned_data['shorname'],
            activo=True
        )
        depa.save()

        #Crear empleado
        #nombre = form.cleaned_data['nombre']
        #apellido = form.cleaned_data['apellidos']      
        
        Empleado.objects.create(
            #firts_name=nombre,
            #last_name=apellido,
            job='1',
            departamento=depa #Asignar el departamento crado
        )
        return super().form_valid(form)
    
    

# Create your views here.
