from django.db import models
from modules.users.models import User

# Create your models here.
CATEGORIA = {
    ('PLA', "Planeación"),
    ('AEI', "Ahorro e inversión"),
    ('CRE', "Crédito"),
    ('SEG', "Seguro"),
    ('APR', "Ahorro para el retiro"),
}

TEMA = {
    ('PRE', "Presupuesto"),
    ('AHO', "Ahorro"),
    ('GAH', "Gasto hormiga"),
    ('IDA', "Instituciones de ahorro"),
    ('INV', "Inversión"),
    ('CRE', "Crédito"),
    ('MCR', "Microcréditos"),
    ('FPE', "Financiamiento para tu empresa"),
    ('IDC', "Instituciones de crédito"),
    ('BDC', "Buró de crédito"),
    ('SEG', "Seguros"),
    ('SOV', "Seguro obligatorio vehicular"),
    ('MSG', "Microseguros"),
    ('RET', "Retiro"),
}

class Contenido(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100,choices=CATEGORIA)
    tema = models.CharField(max_length=100,choices=TEMA)
    otro_tema = models.CharField(max_length=100, null=True, blank=True)
    resumen = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to = "images/")
    url_pdf = models.URLField(blank=True,null=True)
    url_video = models.URLField(blank=True,null=True)


    def __str__(self):
        categ = dict(CATEGORIA)
        tem = dict(TEMA)
        return "Categoría: %s, Tema: %s" % (categ[self.categoria], tem[self.tema])

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    contenidos = models.ManyToManyField(Contenido,blank=True,null=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIA)

    def __str__(self):
        categ = dict(CATEGORIA)
        return "Curso: %s. Categoría: %s" % (self.nombre, categ[self.categoria])

class TrackingEducacion(models.Model):
    id =models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)
    avance = models.DecimalField(max_digits = 5, decimal_places=2, default=0.00)
