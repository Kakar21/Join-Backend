from django.db import models


class Contact(models.Model):
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ManyToManyField(Contact, related_name="task")
    due_date = models.DateField()
    priority = models.CharField(max_length=10)
    category = models.CharField(max_length=15)
    subtasks = models.JSONField(default=list, blank=True)
    subtasks_done = models.JSONField(default=list, blank=True)
    state = models.CharField(max_length=15)

    def __str__(self):
        return self.task_title
