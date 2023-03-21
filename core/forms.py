from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

# Somente os dados (tipo para e-mail)
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150)
    email = forms.EmailField(label='E-mail', max_length=150)
    assunto = forms.CharField(label='Assunto', max_length=150)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def mandar_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject='E-mail enviando pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email},
        )
        mail.send()
        

# Integração com a base de dado
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
    