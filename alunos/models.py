from django.db import models

# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def _str_(self):
        return self.nome