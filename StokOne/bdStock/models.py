from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Conectividad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Impresora(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    conectividad = models.ForeignKey(Conectividad, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class IngresoImpresora(models.Model):
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

class VentaImpresora(models.Model):
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.cantidad > self.impresora.cantidad:
            raise ValueError("No hay suficientes impresoras en stock")
        self.impresora.cantidad -= self.cantidad
        self.impresora.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.impresora.cantidad += self.cantidad
        self.impresora.save()
        super().delete(*args, **kwargs)