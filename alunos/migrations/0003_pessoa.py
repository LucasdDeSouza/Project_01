# Generated by Django 4.2.18 on 2025-02-10 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=50)),
                ('data', models.DateField(max_length=10)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alunos.cidade')),
            ],
        ),
    ]
