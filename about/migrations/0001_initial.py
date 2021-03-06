# Generated by Django 2.0.2 on 2020-08-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('content2', models.TextField(verbose_name='Contenido 2')),
                ('image', models.ImageField(upload_to='about', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de adición')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'acercade',
                'ordering': ['-created'],
            },
        ),
    ]
