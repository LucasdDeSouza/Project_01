
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EmprestimosViewSet
from alunos.views import AlunosViewSet
from alunos.views import LivrosViewSet

router = DefaultRouter()
router.register(r'emprestimos', EmprestimosViewSet)
router.register(r'alunos', AlunosViewSet)
router.register(r'livros', LivrosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
