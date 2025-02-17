from rest_framework.serializers import ModelSerializer
from alunos.models import Livros
from alunos.models import Alunos
from alunos.models import Emprestimos

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class EmprestimosSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'