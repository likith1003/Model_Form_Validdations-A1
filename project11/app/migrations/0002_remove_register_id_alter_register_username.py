# Generated by Django 5.1.1 on 2024-10-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='id',
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]