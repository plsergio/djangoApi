from django.shortcuts import render

def persons_list(request):
    return render(request, 'pessoa.html')
