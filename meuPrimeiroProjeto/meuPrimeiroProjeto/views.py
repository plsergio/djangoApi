from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse('Olá mundo')
    return render(request, 'index.html')
def articles(request, year):
    return  HttpResponse('o ano enviado foi: ' + str(year))

def lerBanco(nome):
    listaNomes= [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquina', 'idade': 40}
    ]

    for pessoa in listaNomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Não encontrado', 'idade': 0}

def fname(request,nome):
    resultado = lerBanco(nome)
    # return HttpResponse(resultado['nome'] + ' com ' + str(resultado['idade']))
    nome = resultado['nome']
    idade = lerBanco(nome)['idade']
    return render(request,'pessoa.html', {'idade': idade, 'nome': nome})