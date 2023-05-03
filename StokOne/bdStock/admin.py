from django.contrib import admin
from bdStock.models import Impresora, Marca, Modelo, Tipo, Conectividad, IngresoImpresora, VentaImpresora
# Register your models here.
class ImpresoraAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','tipo','conectividad','fecha_registro','precio_compra','precio_venta','estado','cantidad')
admin.site.register(Impresora, ImpresoraAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Marca, MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Modelo, ModeloAdmin)

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Tipo, TipoAdmin)

class ConectividadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Conectividad, ConectividadAdmin)

class IngresoImpresoraAdmin(admin.ModelAdmin):
    list_display = ('impresora','fecha','cantidad',)
admin.site.register(IngresoImpresora,IngresoImpresoraAdmin)
class VentaImpresoraAdmin(admin.ModelAdmin):
    list_display = ('impresora','fecha','cantidad',)
admin.site.register(VentaImpresora,VentaImpresoraAdmin)