# Generated by Django 4.1.2 on 2022-10-16 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Revendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carros.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.FloatField(max_length=10)),
                ('ano', models.IntegerField(max_length=4)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carros.modelo')),
            ],
        ),
    ]
