# Generated by Django 4.2.18 on 2025-02-17 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_alunos_emprestimos_livros_remove_pessoa_cidade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='ano_publicação',
            new_name='ano_publicacao',
        ),
    ]
