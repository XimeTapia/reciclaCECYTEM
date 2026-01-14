from django.contrib import admin
from .models import Empleado,Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'firts_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    def full_name(self, obj):
        return obj.firts_name + '' + obj.last_name

    search_fields=('firts_name',)
    list_filter=('departamento','job','habilidades')

    filter_horizontal=('habilidades',)
    
admin.site.register(Empleado,EmpleadoAdmin)

