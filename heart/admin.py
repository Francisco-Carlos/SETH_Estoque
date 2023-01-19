from django.contrib import admin
from .models import Usuarios,Produtos
# Register your models here.

class List_produtos(admin.ModelAdmin):
    list_display = ('Nome','Preco','Quantidade')

class List_Usarios(admin.ModelAdmin):
    list_display = ('Nome','Chapa','Tipo_de_usuario','Senha')

admin.site.register(Produtos,List_produtos)
admin.site.register(Usuarios,List_Usarios)