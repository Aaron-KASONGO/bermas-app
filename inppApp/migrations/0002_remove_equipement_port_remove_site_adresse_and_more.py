# Generated by Django 4.2.6 on 2023-11-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inppApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipement',
            name='port',
        ),
        migrations.RemoveField(
            model_name='site',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='sousreseaux',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='sousreseaux',
            name='adresse_ip',
        ),
        migrations.AddField(
            model_name='equipement',
            name='adresse_ip',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
