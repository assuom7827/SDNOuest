# Generated by Django 3.2.16 on 2023-01-18 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conofo', '0015_auto_20230118_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_TF', models.CharField(max_length=3, verbose_name='Code type de formation')),
                ('intitule_TF_fr', models.CharField(max_length=25, verbose_name='Intitulé de type de formation (En latin)')),
                ('intitule_TF_ar', models.CharField(max_length=25, verbose_name='Intitulé de type de formation (En arabe)')),
            ],
            options={
                'verbose_name': 'Type de formation',
                'verbose_name_plural': 'Types de formation',
            },
        ),
        migrations.AlterField(
            model_name='filieres',
            name='type_formation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conofo.typesformation', verbose_name='Type de la formation'),
        ),
    ]
