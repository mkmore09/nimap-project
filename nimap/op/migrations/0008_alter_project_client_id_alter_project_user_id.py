# Generated by Django 4.0.4 on 2022-09-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0007_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
