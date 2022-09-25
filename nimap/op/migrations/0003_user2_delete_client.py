# Generated by Django 4.0.4 on 2022-09-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0002_client_created_at_client_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='user2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createdby', models.CharField(max_length=100)),
                ('createdat', models.DateTimeField(auto_now=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]