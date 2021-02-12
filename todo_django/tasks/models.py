from django.db import models


class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
    STATUS_CHOICES = (
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default=TODO)

    def __str_(self):
        return f'[{self.status}] {self.title}'
