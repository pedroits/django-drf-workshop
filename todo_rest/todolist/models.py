from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField()

    class Meta:
        db_table = 'list'

class TodoTask(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='tasks')
    summary = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField()
    date_limit = models.DateTimeField()
    info = models.TextField(null=True)
    modified_info = models.TextField(null=True)

    @property
    def atrasado(self):
        if not self.finished and self.date_limit < timezone.now():
            return True

        return False
