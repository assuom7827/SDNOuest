# Generated by Django 3.2.16 on 2023-01-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conofo', '0002_remove_domaines_faculte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filieres',
            name='cycle',
            field=models.CharField(choices=[('L', 'LICENCE'), ('M', 'MASTER'), ('D', 'DOCTEUR'), ('DM', 'Docteur en Médecine'), ('ING', 'Ingénieur')], default='L', max_length=3, null=True, verbose_name='Cycle de filière'),
        ),
        migrations.AlterField(
            model_name='specialites',
            name='cycle',
            field=models.CharField(choices=[('L', 'LICENCE'), ('M', 'MASTER'), ('D', 'DOCTEUR'), ('DM', 'Docteur en Médecine'), ('ING', 'Ingénieur')], default='L', max_length=3, null=True, verbose_name='Cycle de filière'),
        ),
    ]
