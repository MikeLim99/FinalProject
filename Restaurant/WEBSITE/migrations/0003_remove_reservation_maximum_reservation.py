# Generated by Django 5.0.3 on 2024-03-31 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0002_reservation_maximum_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='maximum_reservation',
        ),
    ]