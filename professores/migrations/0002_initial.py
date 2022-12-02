# Generated by Django 4.1.2 on 2022-12-02 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treino',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.aluno'),
        ),
        migrations.AddField(
            model_name='treino',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professor'),
        ),
        migrations.AddField(
            model_name='itemtreino',
            name='exercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.exercicio'),
        ),
        migrations.AddField(
            model_name='itemtreino',
            name='treino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.treino'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='alunos',
            field=models.ManyToManyField(blank=True, to='user.aluno'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.aula'),
        ),
        migrations.AddField(
            model_name='aula',
            name='modalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.modalidade'),
        ),
        migrations.AddField(
            model_name='aula',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professor'),
        ),
    ]
