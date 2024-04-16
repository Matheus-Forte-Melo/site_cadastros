from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST': # Teoricamente eu posso fazer a validação que eu quiser aqui
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nascimento = request.POST.get('nascimento')
        pais = request.POST.get('país')
        

        pessoa = Pessoa(nome=nome, email=email, nascimento=nascimento, pais=pais)
        pessoa.save()
        return redirect("/")
        

    dados = Pessoa.objects.all()[:10]
    context = {'pessoas': dados}
    return render(request, 'home/partial/register.html', context=context)

def atualizar(request, id):
    dados = Pessoa.objects.get(id=id)

    if request.method == 'POST':
        if request.POST.get('nome') != dados.nome:
            dados.nome = request.POST.get('nome')

        if request.POST.get('email') != dados.email:
            dados.email = request.POST.get('email')

        if str(request.POST.get('nascimento')) != str(dados.nascimento):
            dados.nascimento = request.POST.get('nascimento')

        if request.POST.get('país') != dados.pais:
            dados.pais = request.POST.get('país') 

        dados.save()
        return redirect('/')

    context = {'pessoa': dados}
    return render(request, 'home/partial/edit.html', context=context)


def deletar(request, id):

    dados = Pessoa.objects.get(id=id) 

    if request.method == "POST":
        dados.delete()
        return redirect('/')

    
    context = {'pessoa': dados}
    return render(request, 'home/partial/delete.html', context=context)

def detalhado(request):
    if request.method == 'POST':
        pesquisa = request.POST.get('pesquisa')
        dados = Pessoa.objects.filter(nome__icontains=pesquisa)
        context = {'pessoas':dados, 'quant':len(dados)}
        return render(request, "home/partial/detailed.html",context=context)
        

    dados = Pessoa.objects.all()
    context = {'pessoas':dados, 'quant':len(dados)}
    return render(request, "home/partial/detailed.html",context=context)