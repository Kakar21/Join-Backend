from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=255)
    description = models.TextField()
    dueDate = models.DateField()
    priority = models.CharField(max_length=10)
    category = models.CharField(max_length=15)
    state = models.CharField(max_length=15)

    def __str__(self):
        return self.taskTitle
    

class Subtask(models.Model):
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Contact(models.Model):
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name