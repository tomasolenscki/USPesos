# Generated by Django 4.1.3 on 2022-11-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='inscritos',
            field=models.IntegerField(blank=True, default=0, verbose_name='Número de inscritos'),
        ),
    ]
