# Generated by Django 5.1.2 on 2024-11-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('reader', 'Reader'), ('librarian', 'Librarian')], default='reader', max_length=10),
        ),
    ]
