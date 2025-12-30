from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    
    nome = models.CharField(max_length=80,
                    verbose_name='Nome',
                    help_text='Nome completo do usuário',
                    null=False)
    email = models.EmailField(unique=True, 
                    verbose_name='E-mail',
                    help_text='E-mail do usuário',
                    null=False)
    senha = models.CharField(max_length=255,
                    verbose_name='Senha',
                    help_text='Senha do usuário',
                    null=False)
    
    # CAMPOS ADICIONADOS PARA CEP DO USUÁRIO
    cep = models.CharField(max_length=8, 
                    verbose_name='CEP',
                    help_text='CEP do usuário',
                    null=False)
    logradouro = models.CharField(max_length=255,
                    verbose_name='Rua/Avenida',
                    help_text='Logradouro do usuário',
                    blank=True, null=True)
    numero = models.CharField(max_length=10,
                    verbose_name='Número',
                    help_text='Número do endereço',
                    blank=False, null=True) 
    complemento = models.CharField(max_length=255,
                    verbose_name='Complemento',
                    help_text='Complemento do endereço',
                    blank=True, null=True)
    bairro = models.CharField(max_length=100,
                    verbose_name='Bairro',
                    help_text='Bairro do usuário',
                    blank=True, null=True)
    cidade = models.CharField(max_length=100,
                    verbose_name='Cidade',
                    help_text='Cidade do usuário',
                    blank=True, null=True)
    estado = models.CharField(max_length=2, # UF
                    verbose_name='Estado',
                    help_text='Estado (UF) do usuário',
                    blank=True, null=True)
    ativo = models.BooleanField(
                    default=True,
                    verbose_name='Ativo'
    )
    cpf = models.CharField(
        max_length=11,  # só números
        verbose_name='CPF',
        help_text='CPF do usuário sem traços',
        unique=True, null=False
    )
    # --------------------------------------------------
 
    criado = models.DateTimeField(auto_now_add=True,
                    verbose_name='Criado em')
    atualizado = models.DateTimeField(auto_now=True,
                    verbose_name='Atualizado em')
    
    class Meta:
        # nome da tabela
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome'] #ordena por nome (ordem alfabetica)
        # se fosse por data de criação
        # ordering = ['-criado'] 
        # ordem do mais recente (decrescente)
    
    def __repr__(self):
        """
        Retorna uma string representativa do objeto, no formato
        "<nome>".
        """
        return f'<Usuario {self.nome}>'
    
    def __str__(self):
        """
        Retorna uma string representativa do objeto, no formato
        "<nome> (<email>)".
        """
        return f'{self.nome} ({self.email})'

    def verificar_senha(self, senha_texto):
        return check_password(senha_texto, self.senha)
        # a primeira senha é sempre a digitada no momento
        # a segunda senha vem do banco de dados

    def save(self, *args, **kwargs):
        # args = argumentos posicionais
        # kwargs = argumentos nomeados
        if self.senha and not \
        self.senha.startswith('pbkdf2_sha256'):
            # se a senha for alterada
            self.senha = make_password(self.senha)
        # se a senha for criada ou atualizada
        # chama o save da superclasse
        super().save(*args, **kwargs)

    # criar a verificação se o usuário está autenticado
    # Isso faz com que qualquer instancia (objeto) desse
    # modelo seja considerada autenticada pelo Django

    @property
    def is_authenticated(self):
        '''
        Retorna True sempre, pois objetos (usuario) só existem
        se autenticados
        '''
        return True

    @property
    def is_anonymous(self):
        '''
        Retorna False sempre, pois não aceita objeto (usuario)
        anonimo
        Isso infrma ao Django que esse objeto não é do tipo
        especial "AnonymousUser" (que representa usuários não
        logados)
        '''
        return False