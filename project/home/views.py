from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# def home(request):
#     print('home')


#     return render(
#         request,
#         'home.html',
        
#     )

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def doacao_view(request):
    return render(request, 'doacao.html')


#funcao para BD cadastro

#Formulário de cadastro de usuário
def create(request):
    return render(request, '')


#Inserção dos dados do usuário no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'

    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'register.html',data)


#Formulário de login do painel
def painel(request):
    return render(request, '')

#Processar o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha incorretos!'
        data['class'] = 'alert-danger'

        return render(request, 'login.html' , data)


#Pagina inicial do dashboard (main)
def dashboard(request):
    return render(request, 'dashboard/main.html')