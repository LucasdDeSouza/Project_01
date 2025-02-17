from rest_framework.serializers import ModelSerializer
from alunos.models import Estado
from alunos.models import Cidade
from alunos.models import Pessoa

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'