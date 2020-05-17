from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'list'

class NovaEntidade(models.Model):
    name = models.CharField(max_length=255)
    sort = models.IntegerField()

    class Meta:
        db_table = 'nova_entidade'