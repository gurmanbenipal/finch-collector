# Generated by Django 4.2.3 on 2023-07-29 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_feeding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
    ]
