# Generated by Django 4.1.3 on 2022-12-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_professor_cref'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='urlfoto',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL da foto'),
        ),
    ]
