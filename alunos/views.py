from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from alunos.models import Estado
from alunos.models import Cidade
from alunos.models import Pessoa
from alunos.serializers import EstadoSerializer
from alunos.serializers import CidadeSerializer
from alunos.serializers import PessoaSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

