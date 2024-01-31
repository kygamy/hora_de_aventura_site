from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia

from django.contrib import messages

from galeria.forms import FotografiaForms


def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def nova_imagem(request):
    form = FotografiaForms
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova Imagem Adicionada")
            return redirect("index")
    return render(request, "galeria/nova_imagem.html", {"form": form})

def editar_imagem(request):
    pass

def excluir_imagem(request):
    pass