from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("dataFotografia").filter(publicada=True) # podemos utilizar o order_by para ordernar de acordo com o nosso querer, se adicionarmos um "-" a lista se inverse
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-dataFotografia").filter(publicada=True) # podemos utiliz

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']   # esses 'buscar' faz referencia ao name='buscar' no input do index
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)     # verefica se uma parte do que a gente busca fazr sentido no que queremos encontrar

    return render(request, "galeria/buscar.html", { "cards": fotografias })