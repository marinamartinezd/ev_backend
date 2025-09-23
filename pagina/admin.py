from django.contrib import admin
from .models import Usuario
from .models import Empleado
from .models import Mascota

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'user_nombre', 'user_direccion', 'user_telefono', 'get_cargo', 'get_sueldo')
    search_fields = ('id_usuario', 'user_nombre','user_telefono')
    list_filter = ('user_nombre',)
    ordering = ('user_nombre',)

    def get_cargo(self, obj):
        empleado = Empleado.objects.filter(id_usuario=obj).first()
        return empleado.empl_cargo if empleado else "-"
    get_cargo.short_description = "Cargo"

    def get_sueldo(self, obj):
        empleado = Empleado.objects.filter(id_usuario=obj).first()
        return empleado.empl_sueldo if empleado else "-"
    get_sueldo.short_description = "Sueldo"

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'masc_nombre','masc_estado')
    search_fields = ('id_mascota', 'masc_nombre')
    list_filter = ('masc_estado', 'id_especie',)
    ordering = ('masc_nombre',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empleado) 
admin.site.register(Mascota, MascotaAdmin)

# Register your models here.