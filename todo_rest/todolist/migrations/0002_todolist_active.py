# Generated by Django 3.0.6 on 2020-05-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
