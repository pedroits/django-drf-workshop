# Generated by Django 3.0.6 on 2020-05-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_todotask_todo_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='info',
            field=models.TextField(null=True),
        ),
    ]