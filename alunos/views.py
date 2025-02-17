from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from alunos.models import Livros
from alunos.models import Alunos
from alunos.models import Emprestimos
from alunos.serializers import LivrosSerializer
from alunos.serializers import AlunosSerializer
from alunos.serializers import EmprestimosSerializer

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

