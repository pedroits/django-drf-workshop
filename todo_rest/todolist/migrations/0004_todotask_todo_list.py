# Generated by Django 3.0.6 on 2020-05-16 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todotask'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='todo_list',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.TodoList'),
            preserve_default=False,
        ),
    ]
