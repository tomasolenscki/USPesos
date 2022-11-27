# Generated by Django 4.1.2 on 2022-11-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, verbose_name='Dia e hora da aula')),
                ('visível', models.BooleanField(blank=True, verbose_name='Visível')),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, verbose_name='Nome do exercício')),
                ('urlfoto', models.CharField(blank=True, max_length=255, verbose_name='URL da imagem do exercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Itemtreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga', models.IntegerField(blank=True, verbose_name='Carga do exercício')),
            ],
        ),
        migrations.CreateModel(
            name='Treinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(blank=True, verbose_name='Nível de dificuldade')),
                ('comentario', models.TextField(blank=True, verbose_name='Comentários')),
                ('Criado', models.BooleanField(blank=True, default=False, verbose_name='Já foi montado?')),
                ('Itens_treino', models.ManyToManyField(blank=True, to='professores.itemtreino')),
            ],
        ),
    ]
