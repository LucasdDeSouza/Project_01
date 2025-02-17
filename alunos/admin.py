from django.contrib import admin

# Register your models here.
from .models import Livros
from .models import Alunos
from .models import Emprestimos

admin.site.register(Livros)
admin.site.register(Alunos)
admin.site.register(Emprestimos)