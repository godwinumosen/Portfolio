# Generated by Django 4.1.4 on 2023-07-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_usermodel_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='fistname',
            new_name='firstname',
        ),
    ]
