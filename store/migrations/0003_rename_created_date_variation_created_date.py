# Generated by Django 4.1.3 on 2023-01-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='created_DAte',
            new_name='created_Date',
        ),
    ]
