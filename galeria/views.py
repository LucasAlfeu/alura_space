from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) # podemos utilizar o order_by para ordernar de acordo com o nosso querer, se adicionarmos um "-" a lista se inverse
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})