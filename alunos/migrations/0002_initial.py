# Generated by Django 4.1.2 on 2022-12-02 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessao',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.aluno'),
        ),
    ]
