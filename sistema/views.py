from django.shortcuts import render

# aqui irao ficar todas as views (controladores) referente ao app sistema
# a funçao index informa o que vai acontecer quando ela for chamada
def index(request): #funçao esperando uma requisiçao
    return render(
        request,
        'sistema/index.html',
    )


