from django.shortcuts import render
from .forms import ContatoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm()
    
    
    return render(request, 'contato.html', {'form': form})

def produto(request):
    return render(request, 'produto.html')
