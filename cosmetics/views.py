from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

@login_required
def dashboard(request):
    produtos = Produto.objects.all()
    return render(request, 'dashboard.html', {'produtos': produtos})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('dashboard')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, f"O produto '{produto.nome}' foi atualizado!")
            return redirect('dashboard')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    nome_produto = produto.nome
    produto.delete()
    messages.warning(request, f"Produto '{nome_produto}' excluído com sucesso.")
    return redirect('dashboard')

from rest_framework import viewsets
from .serializers import ProdutoSerializer
from .models import Produto

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
from django.shortcuts import render
from .models import Produto

from django.shortcuts import render
from .models import Dica

def dicas(request):
    todas_as_dicas = Dica.objects.all().order_by('-criado_em')
    
    contexto = {
        'dicas': todas_as_dicas, 
        'instagram': '@princefound_cosmeticos',
        'whatsapp': '(31) 98765-4321 🐸',
        'email_contato': 'contato@princefound.com.br',
    }
    return render(request, 'dicas.html', contexto)