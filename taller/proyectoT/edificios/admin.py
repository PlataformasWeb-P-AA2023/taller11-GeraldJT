from django.contrib import admin


from edificios.models import *


class EdificioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
 
    list_display = ('nombre_Propietario', 'costo', 'numero_cuartos', 'edificio')
    #raw_id_fields = ('departamento',)
    search_fields = ('nombre_Propietario', 'costo')
admin.site.register(Departamento, DepartamentoAdmin)
