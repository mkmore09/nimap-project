# Generated by Django 4.0.4 on 2022-09-22 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0003_user2_delete_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user2',
            new_name='Client',
        ),
    ]