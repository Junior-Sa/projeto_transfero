from django.shortcuts import render

# aqui irao ficar todas as views controladores referente ao sistema

def index(request): #funçao esperando uma requisiçao
    return render(
        request,
        'sistema/index.html',
    )


