from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50, editable=True)
    subnombre = models.CharField('Nombre_corto', max_length=50, unique=True)
    activo= models.BooleanField('Anulado', default='false')
 
    class Meta:
        verbose_name='Mi departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['-nombre']
        unique_together=('nombre','subnombre')
    
    def __str__(self):
        return str(self.id)+ '-'+ self.nombre +'-' + self.subnombre