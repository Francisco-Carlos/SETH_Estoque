<p align='center'>
<img src="https://user-images.githubusercontent.com/30003984/213574398-fde2015b-737d-4407-a227-d0a274813712.png">
</p>

<h1 align="center">Site de Estoque</h1>
<p align="center">Site de controle de estoque simples</p>
<p align="center"> <img src="https://img.shields.io/static/v1?label=Python&message=3.10&color=7159c1&style=for-the-badge&logo=ghost"/>
<img src="https://img.shields.io/static/v1?label=Django&message=1.5.2&color=7159c1&style=for-the-badge&logo=ghost"/> </p>

<p align="center">
 <a href="#Sobre">Sobre </a> :skull:
 <a href="#Funcionamento">Como fuciona </a>:skull:
 <a href="#Imagens">Usuario</a>:skull:
 <a href="#Imagens">Aministrador</a>:skull:
 <a href="#Codigos">Codigos </a>:skull:


<h4 align="center"> 
	 Python 🚀 Concluido...  
</h4>

<h2 align="center" id="Sobre">Sobre</h2>
<p> O projeto e simples o foco em mostrar um controle de estoque fácil e intuitivo com usuários padrão que entra com a seu
usuário e senha e tem alguns privilégios e tem os administradores que tem mais liberdade de alterar os produtos. </p>



<h2 align="center" id="Funcionamento"> Funcionamento </h2>
<p> O site e bem direto tem sua tela de login já pedindo a chapa e a senha do usuário, dependo do usuário fornecido vai ter mais liberdade 
no site</p>
<p align="center">
    <img src="https://user-images.githubusercontent.com/30003984/213576177-09fb3ac9-7c31-46f5-bb25-3d7f50a703f8.png">
</p>

<h2 align="center" id="Imagens"> Usuario padrão</h2>
<p> O usuário padrão poderá fazer pesquisas e baixar o arquivo em excel, dessa forma poderá passar essa informação por e-mail
ou fazer uma alteração no excel pedindo por produtos ou solicitando a troca do valor da mercadoria sem fazer alterações no site.</p>

![Seth_usuario](https://user-images.githubusercontent.com/30003984/213576523-0271c515-ec02-4622-8f50-ea8d4f63c5e4.png)


<h2 align="center" id="Imagens"> Adminstrador</h2>
<p> Administrador usando essa conta pode além da pesquisar os produtos também
pode baixar o arquivo em excel deletar os produtos e também alterar o valor de cada um.</p>

![Seth_admin](https://user-images.githubusercontent.com/30003984/213587310-3f9ba28d-717c-40d5-b53c-67d5136d9c3c.png)
![Seth_admin_excel](https://user-images.githubusercontent.com/30003984/213587440-86ffd5f6-558c-4c99-b67c-ebfc85f80f81.png)
![Seth_admin_alterar](https://user-images.githubusercontent.com/30003984/213587459-faf4614d-3f9a-4a95-9eca-0f9b05f70705.png)



<h2 align="center" id="Codigos"> Codigo </h2>
*** <p>Model</p> ***

```from django.db import models

class Produtos(models.Model):
    Nome = models.CharField(max_length=100)
    Preco = models.DecimalField(max_digits=100,decimal_places=2)
    Quantidade = models.IntegerField()


class Tipos_Contas(models.Model):
    choice = (('ADM','Administrador'),('USR','Usuarios'))
    Tipo = models.CharField(choices=choice,max_length=100)


class Usuarios(models.Model):
    choice = (('ADM', 'Administrador'), ('USR', 'Usuarios'))
    Nome = models.CharField(max_length=100)
    Chapa = models.IntegerField()
    Senha = models.CharField(max_length=8)
    Tipo_de_usuario = models.CharField(choices=choice, max_length=100)
 ```
    
***<p>Views</p>***

```from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .models import Usuarios, Produtos
import xlwt
# Create your views here.

def Index(request):
    return render(request,'Index.html')

def Login(request):
    if request.method == 'POST':
        chapa = request.POST['Chapa']
        senha = request.POST['Senha']
        us = Usuarios.objects.get(Chapa=chapa)
        if us.Senha == senha and us.Tipo_de_usuario == 'ADM' :
            return redirect('Administrador')
        elif us.Senha== senha and us.Tipo_de_usuario== 'USR':
            return redirect('Usuario')
    return redirect('index')

def Sair(request):
    return redirect('index')

def Usuario(request):
    prod = Produtos.objects.all()
    context = {'produtos':prod}
    return render(request,'Usuario.html',context)


def Administrador(request):
    prod = Produtos.objects.all()
    context = {'produtos':prod}
    return render(request,'Administrador.html',context)


#pesquisar
def Pesq(request):

    if request.method == 'POST':
        pesq = request.POST['pesquisa']
        prod = Produtos.objects.filter(Nome__icontains=pesq)
        context = {'produtos':prod}
        return render(request,'Usuario.html',context)

def Pesq_adm(request):

    if request.method == 'POST':
        pesq = request.POST['pesquisa']
        prod = Produtos.objects.filter(Nome__icontains=pesq)
        context = {'produtos':prod}
        return render(request,'Administrador.html',context)

#Deletar
def Deletar(request,id):
    prod = Produtos.objects.get(id=id)
    prod.delete()
    return redirect('Administrador')

#trocar o valor do produto
def Alterar(request,id):
    prod = Produtos.objects.get(id=id)
    context = {'produto':prod}
    if request.POST:
        val = request.POST['novo_valor']
        prod.Preco = val
        prod.save()
        return redirect('Administrador')
    return render(request,'Produto.html',context)

def Valor(request,id):
    prod = Produtos.objects.get(id=id)
    if request.POST:
        val = request.POST['novo_valor']
        prod.Preco = val
        print(prod.Preco)
#exel
def Excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Produtos.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Produtos')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    colunas = ['Nome','Preco','Quantidade']

    for col_num in range(len(colunas)):
        ws.write(row_num,col_num,colunas[col_num],font_style)

    font_style = xlwt.XFStyle()

    linhas = Produtos.objects.all().values_list('Nome','Preco','Quantidade')
    for lin in linhas:
        row_num += 1
        for col_num in range(len(lin)):
            ws.write(row_num,col_num,lin[col_num],font_style)
    wb.save(response)

    return response
```
### As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

