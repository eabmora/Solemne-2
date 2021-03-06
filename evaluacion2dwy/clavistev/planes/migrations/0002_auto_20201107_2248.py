# Generated by Django 3.1.3 on 2020-11-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanHogar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Plan')),
                ('tipoPlan', models.CharField(max_length=20)),
                ('p_internet', models.BooleanField(default=False, verbose_name='¿Posee Internet?')),
                ('p_fibraOptica', models.BooleanField(default=False, verbose_name='¿Posee Fibra Optica')),
                ('p_tvCable', models.BooleanField(default=False, verbose_name='¿Posee TV Cable?')),
                ('p_canalesPremium', models.BooleanField(default=False, verbose_name='¿Posee Canales Premium')),
                ('p_telefoniaFija', models.BooleanField(default=False, verbose_name='¿Posee Telefonia Fija')),
                ('price', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PlanMovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Plan')),
                ('tipoPlan', models.CharField(max_length=20)),
                ('p_internetMovilIlimitado', models.BooleanField(default=False, verbose_name='¿Posee Internet Movil Ilimitado?')),
                ('p_minutosLibres', models.BooleanField(default=False, verbose_name='¿Posee Minutos Libres?')),
                ('p_redesSocialesGratis', models.BooleanField(default=False, verbose_name='¿Posee Redes Sociales Gratis?')),
                ('price', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
