# Generated by Django 4.1.6 on 2023-02-15 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]