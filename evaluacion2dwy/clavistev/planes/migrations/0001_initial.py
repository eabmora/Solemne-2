# Generated by Django 3.1.3 on 2020-11-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Plan')),
                ('p_internet', models.BooleanField(default=False, verbose_name='¿Posee Internet?')),
                ('p_fibraOptica', models.BooleanField(default=False, verbose_name='¿Posee Fibra Optica')),
                ('tipoPlan', models.CharField(choices=[('Plan Hogar', 'Plan Hogar'), ('Plan Movil', 'Plan Movil')], max_length=20)),
            ],
        ),
    ]
