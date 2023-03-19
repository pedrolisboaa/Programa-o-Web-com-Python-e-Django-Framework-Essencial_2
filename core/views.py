from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProduutoModelForm

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
    
    if str(request.method) == 'POST':
        form = ProduutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            
            print(f' Nome: {prod.nome}')
            print(f' Preco: {prod.preco}')
            print(f' Estoque: {prod.estoque}')
            print(f' Imagem: {prod.imagem}')
            
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProduutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar')
    else:
        form = ProduutoModelForm()
        
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)
