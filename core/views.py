from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.mandar_email()
            messages.success(request, 'E-mail enviando com sucesso.')
            form = ContatoForm()    
    else:
        messages.error(request, 'Erro ao enviar e-mai.')
    
    return render(request, 'contato.html', {'form': form})

def produto(request):
    return render(request, 'produto.html')
