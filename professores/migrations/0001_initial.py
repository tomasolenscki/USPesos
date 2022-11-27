# Generated by Django 4.1.2 on 2022-11-27 21:55

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
                ('dia', models.DateField(blank=True, verbose_name='Dia da aula')),
                ('hora', models.TimeField(blank=True, verbose_name='Horário da aula')),
                ('duracao', models.IntegerField(blank=True, default=0, verbose_name='Duração da aula')),
                ('vagas', models.IntegerField(blank=True, default=0, verbose_name='Número de vagas')),
                ('visivel', models.BooleanField(blank=True, verbose_name='Visível')),
                ('modalidade', models.CharField(blank=True, max_length=255, verbose_name='Modalidade da aula')),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, verbose_name='Nome do exercício')),
                ('urlfoto', models.CharField(blank=True, max_length=255, verbose_name='URL da imagem do exercicio')),
                ('maquina', models.CharField(blank=True, max_length=255, verbose_name='Nome da máquina')),
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
                ('repeticao', models.IntegerField(blank=True, verbose_name='Número de repetições')),
            ],
        ),
        migrations.CreateModel(
            name='Treinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(blank=True, verbose_name='Nível de dificuldade')),
                ('comentario', models.TextField(blank=True, verbose_name='Comentários')),
                ('criado', models.BooleanField(blank=True, default=False, verbose_name='Já foi montado?')),
                ('Itens_treino', models.ManyToManyField(blank=True, to='professores.itemtreino')),
            ],
        ),
    ]
