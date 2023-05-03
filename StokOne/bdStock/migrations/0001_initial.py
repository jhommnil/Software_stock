# Generated by Django 4.1.7 on 2023-03-30 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conectividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(default=0)),
                ('conectividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.conectividad')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VentaImpresora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('impresora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.impresora')),
            ],
        ),
        migrations.CreateModel(
            name='IngresoImpresora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('impresora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.impresora')),
            ],
        ),
        migrations.AddField(
            model_name='impresora',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.marca'),
        ),
        migrations.AddField(
            model_name='impresora',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.modelo'),
        ),
        migrations.AddField(
            model_name='impresora',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdStock.tipo'),
        ),
    ]
