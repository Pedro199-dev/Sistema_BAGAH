# Generated by Django 2.0.2 on 2020-07-24 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
    ]