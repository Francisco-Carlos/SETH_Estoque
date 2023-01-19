from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index, name='index'),
    path('login',views.Login, name='login'),
    path('Sair',views.Sair,name='Sair'),
    path('Usuario',views.Usuario, name='Usuario'),
    path('Administrador',views.Administrador, name='Administrador'),

    #Url para modificaoes como deletar e trocar o valor
    #para fazer o deletar e ' o nome da pagina que vai exemplo: deletar/int<id>'
    path('deletar/int<id>',views.Deletar,name='deletar'),
    path('alterar/int<id>',views.Alterar,name='alterar'),
    path('valor/int<id>',views.Valor,name='valor'),
    path('pesq',views.Pesq, name='pesq'),
    path('pesq_adm',views.Pesq_adm, name='pesq_adm'),

    #Exel
    path('excel',views.Excel, name='excel')
]