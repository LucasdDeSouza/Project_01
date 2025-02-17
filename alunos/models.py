from django.db import models


class Livros(models.Model):
    id = models.primary_key=True
    ano_publicacao = models.DateField(max_length=50)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"

class Alunos(models.Model):
    id = models.primary_key=True
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} {self.matricula} {self.curso} "

class Emprestimos(models.Model):
    nome = models.CharField(max_length=50)
    data_emprestimo = models.DateField(max_length=50)
    data_devolucao = models.DateField(max_length=50)
    id_livro = models.ForeignKey(Livros, on_delete=models.PROTECT)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id_aluno} {self.id_livro} {self.data_emprestimo} {self.data_devolucao}"