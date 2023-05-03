from django.shortcuts import render
from bdStock.models import Impresora
# Create your views here.
def AgregarImpresoras(request):
    if request.method == 'POST':
        Marca = request.POST['marca']
        Tipo = request.POST['tipo']
        Conectividad = request.POST['conectividad']
        Fecha_registro = request.POST['fecha_registro']
        Precio_compra = request.POST['precio_compra']
        Precio_venta = request.POST['precio_venta']
        Estado = request.POST['estado']
        Cantidad = request.POST['cantidad']

        registroImpresoras=Impresora(marca=Marca,tipo=Tipo,conectividad=Conectividad,fecha_registro=Fecha_registro,precio_compra=Precio_compra,precio_venta=Precio_venta,estado= Estado,cantidad=Cantidad)
        return render(request,"AgregarImpresoras.html")
    return render(request,"AgregarImpresoras.html")
