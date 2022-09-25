# Generated by Django 4.0.4 on 2022-09-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0006_alter_user2_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('client_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('project_createdby', models.CharField(max_length=100)),
                ('project_createdat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]