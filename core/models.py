from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.IntegerField()
    cpf = models.IntegerField()
    data_nascimento = models.DateTimeField(verbose_name='Data de Nascimento')
    # inserir -> email = models.EmailField(verbose_name='Endereco de Email')
    # inserir -> foto do colaborador
    endereco = models.TextField(max_length=100, verbose_name='Endereco Completo')
    uf = models.CharField(max_length=2)
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criacao')
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    cep = models.IntegerField()
    contato = models.IntegerField()
    ctps = models.IntegerField(verbose_name='Carteira de Trabalho')
    pis = models.IntegerField()
    matricula = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    unidade = models.CharField(max_length=50)
    centro_custo = models.CharField(max_length=15, verbose_name='Centro de Custo')
    local_adm = models.ForeignKey(User, on_delete=models.CASCADE)
    honorario = models.IntegerField()
    codigo_banco = models.IntegerField()
    agencia = models.IntegerField()
    conta = models.IntegerField()
    tipo_conta = models.CharField(max_length=20, verbose_name='Tipo da Conta')
    tipo_pix = models.CharField(max_length=20, verbose_name='Tipo de Chave')
    pix = models.CharField(max_length=25, verbose_name='Chave Pix')
    cartao_alelo = models.CharField(max_length=5, verbose_name='Cartao Alelo')
    n_alelo = models.IntegerField(verbose_name='Numero Cartao Alelo')
    v_alelo = models.IntegerField(verbose_name='Valor Creditado Alelo')
    # inserir -> validade do cartao
    cartao_combustivel = models.CharField(max_length=5, verbose_name='Cartao Combustivel')
    n_combustivel = models.IntegerField(verbose_name='Numero Cartao Combustivel')
    v_combustivel = models.IntegerField(verbose_name='Valor Creditado Combustivel')
    cartoes = models.CharField(max_length=5, verbose_name='Outros Cartoes')
    outros_cartoes = models.CharField(max_length=50, verbose_name='Quais Outros')
    contem_celular = models.CharField(max_length=5, verbose_name='Celular da Empresa')
    serie_celular = models.CharField(max_length=25, verbose_name='Numero de Serie')
    numero_celular = models.IntegerField()
    contem_nb = models.CharField(max_length=5, verbose_name='Notebook da Empresa')
    serie_nb = models.CharField(max_length=25, verbose_name='Numero de Serie - NB')
    patrimonio_nb = models.IntegerField()


class Meta:
    db_table = 'Colaboradores'

    def __str__(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_novocolaborador(self):
        return self.data_nascimento.strftime('%Y-%m-%dT%H:%M')