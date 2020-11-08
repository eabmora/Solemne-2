from django.db import models

# Create your models here.

class Plan(models.Model):

    eleccion_nombre_plan =(
        ('Plan XS', 'Plan XS'),
        ('Plan S', 'Plan S'),
        ('Plan M', 'Plan M'),
        ('Plan L', 'Plan L'),
        ('Plan XL', 'Plan XL')

    )

    eleccion_tipo_plan =(
        ('Plan Hogar', 'Plan Hogar'),
        ('Plan Movil', 'Plan Movil')
    )

    name = models.CharField(verbose_name="Nombre del Plan", max_length=50, choices=eleccion_nombre_plan)
    tipoPlan = models.CharField(verbose_name="Tipo de Plan", max_length=20, choices=eleccion_tipo_plan)
    p_internet = models.BooleanField(default=False, verbose_name="¿Posee Internet?")
    p_fibraOptica = models.BooleanField(default=False, verbose_name="¿Posee Fibra Optica")
    p_tvCable = models.BooleanField(default=False, verbose_name="¿Posee TV Cable?")
    p_canalesPremium = models.BooleanField(default=False, verbose_name="¿Posee Canales Premium")
    p_telefoniaFija = models.BooleanField(default=False, verbose_name="¿Posee Telefonia Fija")
    p_internetMovilIlimitado = models.BooleanField(default=False, verbose_name="¿Posee Internet Movil Ilimitado?")
    p_minutosLibres = models.BooleanField(default=False, verbose_name="¿Posee Minutos Libres?")
    p_redesSocialesGratis = models.BooleanField(default=False, verbose_name="¿Posee Redes Sociales Gratis?")
    price = models.IntegerField(default=1, verbose_name="Precio")


    def __str__(self):
        return '%s %s' % (self.name, self.tipoPlan)

    def generarDescuento(self):
        if (self.price <= 15990):
            return 0.05
        if (self.price <= 22990):
            return 0.1
        if (self.price <= 29990):
            return 0.2
        if (self.price <= 35990):
            return 0.4
        
        return 0.5

    def calcularPrecioFinal(self):
        return self.price * (1.0 - self.generarDescuento())



