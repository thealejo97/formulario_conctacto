# Generated by Django 4.2.1 on 2023-05-11 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=50, unique=True, verbose_name='Apellido*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='casa_apto',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Casa/Apto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ciudad', to='cities_light.city', verbose_name='Ciudad*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='Dirección*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_de_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otra'), ('N', 'Preferiría no contestar')], max_length=10, verbose_name='Sexo*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='pais', to='cities_light.country', verbose_name='País*'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='region', to='cities_light.region', verbose_name='Departamento*'),
        ),
    ]