# Generated by Django 5.0.7 on 2024-08-12 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Style',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='service',
            new_name='style',
        ),
    ]
