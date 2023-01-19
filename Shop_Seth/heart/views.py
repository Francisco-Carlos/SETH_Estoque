from django.contrib.auth import login
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