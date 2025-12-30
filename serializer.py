from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer completo para o modelo Produto.
    Responsável por:
    - Serializar e desserializar dados
    - Validar entradas
    - Criar e atualizar instâncias do modelo
    """

    class Meta:
        model = Produto

        # Campos explicitamente definidos (boa prática)
        fields = [
            'id',
            'nome',
            'marca',
            'preco',
            'descricao',
            'estoque',
            'ativo',
            'criado',
            'atualizado'
        ]

        # Campos somente leitura
        read_only_fields = ['id', 'criado', 'atualizado']

        # Configurações extras de validação
        extra_kwargs = {
            'nome': {
                'required': True,
                'allow_blank': False,
                'max_length': 80,
                'error_messages': {
                    'blank': 'O nome do produto não pode estar vazio.',
                    'required': 'O nome do produto é obrigatório.'
                }
            },
            'marca': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'blank': 'A marca não pode estar vazia.',
                    'required': 'A marca é obrigatória.'
                }
            },
            'preco': {
                'required': True,
                'error_messages': {
                    'required': 'O preço é obrigatório.',
                    'invalid': 'Informe um valor numérico válido.'
                }
            },
            'descricao': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'blank': 'A descrição não pode estar vazia.',
                    'required': 'A descrição é obrigatória.'
                }
            }
        }

    """
    read_only_fields =	Impede alteração de campos

    required = 	Torna o campo obrigatório

    allow_blank = Proíbe string vazia

    error_messages = Personaliza erros

    extra_kwargs = Configura campos sem recriá-los

    """

    # ============================
    # Validações por campo
    # ============================

    def validate_preco(self, value):
        """
        Validação específica do campo preço
        """
        if value <= 0:
            raise serializers.ValidationError(
                'O preço deve ser maior que zero.'
            )
        return value

    def validate_nome(self, value):
        """
        Validação específica do nome
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                'O nome deve ter pelo menos 3 caracteres.'
            )
        return value
    
    def validate_marca(self, value):
        """
        Validação específica do nome
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                'A marca deve ter pelo menos 3 caracteres.'
            )
        return value
    
    def validate_descricao(self, value):
        if len(value) < 3:
            # ERRO AQUI: Deve ser 'serializers' (o nome da biblioteca importada)
            raise serializers.ValidationError( 
                'A Descrição deve ter pelo menos três caracteres'
            )
        return value

    # ============================
    # Validação geral do objeto
    # ============================

    def validate(self, data):
        """
        Validação cruzada entre campos
        """
        nome = data.get('nome')
        marca = data.get('marca')

        if nome and marca and nome.lower() == marca.lower():
            raise serializers.ValidationError(
                'O nome do produto não pode ser igual à marca.'
            )

        return data

    # ============================
    # Métodos de criação e atualização
    # ============================

    def create(self, validated_data):
        """
        Cria um novo produto
        """
        produto = Produto.objects.create(**validated_data)
        return produto

    def update(self, instance, validated_data):
        """
        Atualiza um produto existente
        """
        instance.nome = validated_data.get('nome', instance.nome)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.preco = validated_data.get('preco', instance.preco)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.estoque = validated_data.get('estoque', instance.estoque)
        instance.ativo = validated_data.get('ativo', instance.ativo)

        instance.save()
        return instance