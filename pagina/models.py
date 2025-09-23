from django.db import models

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=6)
    username = models.CharField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=40, null=True, blank=True)
    user_nombre = models.CharField(max_length=40, null=True, blank=True)
    user_apellido = models.CharField(max_length=40, null=True, blank=True)
    user_telefono = models.CharField(max_length=15, null=True, blank=True)
    user_correo = models.EmailField(max_length=100, unique=True)
    user_direccion = models.CharField(max_length=255, null=True, blank=True)
    user_fechanac = models.DateField(null=True, blank=True)
    user_fechareg = models.DateField(null=True, blank=True)
    user_rol = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
    
        db_table = 'USUARIO'

    def __str__(self):
        return self.user_nombre or f"Usuario {self.id_cliente}"

##################################################################################################

class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=6)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field='id_usuario')
    empl_fechacontrato = models.DateField(null=True, blank=True)
    empl_cargo = models.CharField(max_length=24, null=True, blank=True)
    empl_sueldo = models.IntegerField()

    class Meta:
    
        db_table = 'EMPLEADO'

    def __str__(self):
        return f"Empleado {self.id_empleado}"

##################################################################################################

class Sede(models.Model):
    id_sede = models.CharField(primary_key=True, max_length=6)
    sed_nombre = models.CharField(max_length=40, null=True, blank=True)
    sed_region = models.CharField(max_length=40, null=True, blank=True)
    sed_comuna = models.CharField(max_length=40, null=True, blank=True)
    sed_direccion = models.CharField(max_length=255, null=True, blank=True)
    sed_correo = models.EmailField(max_length=100, unique=True)
    sed_numero = models.CharField(max_length=15, null=True, blank=True)
    sed_capacidad = models.IntegerField()

    class Meta:
    
        db_table = 'SEDE'

    def __str__(self):
        return f"Sede {self.id_sede}"

##################################################################################################

class Especie(models.Model):
    id_especie = models.CharField(primary_key=True, max_length=6)
    espe_nombre = models.CharField(max_length=40, null=True, blank=True)
    espe_raza = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
    
        db_table = 'ESPECIE'

    def __str__(self):
        return self.espe_nombre or f"Especie {self.id_especie}"
    
##################################################################################################

class Mascota(models.Model):
    id_mascota = models.CharField(primary_key=True, max_length=6)
    id_especie = models.ForeignKey('Especie', on_delete=models.CASCADE, to_field='id_especie')
    id_sede = models.ForeignKey('Sede', on_delete=models.CASCADE, to_field='id_sede')
    masc_historial = models.CharField(max_length=255, null=True, blank=True)
    masc_sexo = models.CharField(max_length=15, null=True, blank=True)
    masc_edad = models.CharField(max_length=3, null=True, blank=True)
    masc_nombre = models.CharField(max_length=40, null=True, blank=True)
    masc_descripcion = models.CharField(max_length=40, null=True, blank=True)
    masc_fechaintroduccion = models.DateField(null=True, blank=True)
    masc_estado = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
    
        db_table = 'MASCOTA'

    def __str__(self):
        return self.masc_nombre or f"Mascota {self.id_mascota}"

##################################################################################################

class Visita(models.Model):
    id_visita = models.CharField(primary_key=True, max_length=6)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field='id_usuario')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, to_field='id_mascota')
    id_sede = models.ForeignKey('Sede', on_delete=models.CASCADE, to_field='id_sede')
    visi_fecha = models.DateField(null=True, blank=True)
    visi_Estado = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
    
        db_table = 'VISITA'

    def __str__(self):
        return f"Visita {self.id_visita}"

##################################################################################################

class Solicitud(models.Model):
    id_solicitud = models.CharField(primary_key=True, max_length=6)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field='id_usuario')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, to_field='id_mascota')
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, to_field='id_empleado')
    id_sede = models.ForeignKey('Sede', on_delete=models.CASCADE, to_field='id_sede')
    soli_descripcion = models.CharField(max_length=255, null=True, blank=True)
    soli_fecha = models.DateField(null=True, blank=True)
    soli_comision = models.IntegerField() 
    soli_estado = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
    
        db_table = 'SOLICITUD'

    def __str__(self):
        return f"Solicitud {self.id_solicitud}"

##################################################################################################

class BlogPost(models.Model):
    id_post = models.CharField(primary_key=True, max_length=100)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field='id_usuario')
    post_categoria = models.CharField(max_length=50, null=False, blank=False) 
    post_titulo = models.CharField(max_length=255, null=False, blank=False) 
    contenido = models.CharField(max_length=255, null=False, blank=False) 
    post_fecha = models.DateField(null=True, blank=True)

    class Meta:
    
        db_table = 'BLOGPOST'

    def __str__(self):
        return f"BlogPost {self.id_post}"