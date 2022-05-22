from django.shortcuts import render, redirect
from core.models import Colaborador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def modulos(request):
    return render(request, 'modulos.html')

@login_required(login_url='/login/')
def contratos(request):
    return render(request, 'dash.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/modulos')
        else:
            messages.error(request, "Usuário ou senha inválido!")
    return redirect('/')


@login_required(login_url='/login/')
def lista_colaboradores(request):
    usuario = request.user
    colaborador = Colaborador.objects.filter(local_adm=usuario)[:4]
    dados = {'colaboradores': colaborador}
    return render(request, 'colaboradores.html', dados)


# listar todos os colaboradores do usuario
@login_required(login_url='/login/')
def todos_colaboradores(request):
    usuario = request.user
    colaboradores = Colaborador.objects.filter(local_adm=usuario)
    dados = {'colaboradores': colaboradores}
    return render(request, 'todoscolaboradores.html', dados)


@login_required(login_url='/login/')
def novocolaborador(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['novocolaborador'] = Colaborador.objects.get(id=id_evento)
    return render(request, 'novocolaborador.html', dados)

@login_required(login_url='/login/')
def submit_alelo(request, id_evento):
    if request.POST:
        id = request.POST.get('id_evento')
        n_alelo = request.POST.get('n_alelo')
        v_alelo = request.POST.get('v_alelo')
        Colaborador.objects.filter(id=id).update(n_alelo=n_alelo,
                                                 v_alelo=v_alelo)
    return redirect('/')

@login_required(login_url='/login/')
def submit_pagamento(request, id_evento):
    if request.POST:
        id = request.POST.get('id_evento')
        agencia = request.POST.get('agencia')
        conta = request.POST.get('conta')
        codigo_banco = request.POST.get('codigo_banco')
        Colaborador.objects.filter(id=id).update(agencia=agencia,
                                                 codigo_banco=codigo_banco,
                                                 conta=conta)
    return redirect('/')    

@login_required(login_url='/login/')
def submit_novocolaborador(request):
    if request.POST:
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        cargo = request.POST.get('cargo')
        cpf = request.POST.get('cpf')
        contato = request.POST.get('contato')
        rg = request.POST.get('rg')
        uf = request.POST.get('uf')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        unidade = request.POST.get('unidade')
        usuario = request.user
        matricula = request.POST.get('matricula')
        id_evento = request.POST.get('id_evento')
        cep = request.POST.get('cep')
        ctps = request.POST.get('ctps')
        pis = request.POST.get('pis')
        carga_horaria = request.POST.get('carga_horaria')
        endereco = request.POST.get('endereco')
        centro_custo = request.POST.get('centro_custo')
        tipo_pix = request.POST.get('tipo_pix')
        pix = request.POST.get('pix')
        honorario = request.POST.get('honorario')
        if id_evento:
            Colaborador.objects.filter(id=id_evento).update(nome=nome,
                                                            data_nascimento=data_nascimento,
                                                            cargo=cargo,
                                                            cpf=cpf,
                                                            contato=contato,
                                                            rg=rg,
                                                            uf=uf,
                                                            cidade=cidade,
                                                            bairro=bairro,
                                                            unidade=unidade,
                                                            tipo_pix=tipo_pix,
                                                            pix=pix,
                                                            honorario=honorario)
        else:
            Colaborador.objects.create(nome=nome,
                                       data_nascimento=data_nascimento,
                                       cargo=cargo,
                                       cpf=cpf,
                                       cep=cep,
                                       endereco=endereco,
                                       contato=contato,
                                       rg=rg,
                                       uf=uf,
                                       cidade=cidade,
                                       centro_custo=centro_custo,
                                       bairro=bairro,
                                       unidade=unidade,
                                       matricula=matricula,
                                       ctps=ctps,
                                       pis=pis,
                                       tipo_pix=tipo_pix,
                                       pix=pix,
                                       carga_horaria=carga_horaria,
                                       honorario=honorario,
                                       local_adm=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_colaborador(request, id_evento):
    usuario = request.user
    colaborador = Colaborador.objects.get(id=id_evento)
    if usuario == colaborador.local_adm:
        colaborador.delete()

    return redirect('/')

@login_required(login_url='/login/')
def adicionar_alelo(request, id_evento):
    colaborador = Colaborador.objects.get(id=id_evento)
    dados = {'colaboradores': colaborador}
    return render(request, 'alelo.html', dados)

@login_required(login_url='/login/')
def adicionar_pagamento(request, id_evento):
    colaborador = Colaborador.objects.get(id=id_evento)
    dados = {'colaboradores': colaborador}
    return render(request, 'pagamento.html', dados)

@login_required(login_url='/login/')
def dados_colaborador(request, id_evento):
    usuario = request.user
    colaborador = Colaborador.objects.get(id=id_evento)
    dados = {'colaboradores': colaborador}
    if usuario == colaborador.local_adm:
        return render(request, 'dados.html', dados)
    else:
        return redirect('/')
