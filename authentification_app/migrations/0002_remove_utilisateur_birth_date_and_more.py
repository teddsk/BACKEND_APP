# Generated by Django 5.0.7 on 2025-03-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='username',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
