# Generated by Django 4.2.11 on 2024-10-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0006_alter_printjob_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='Bloqué'),
        ),
    ]
