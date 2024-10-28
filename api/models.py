from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Stores contact information with a name, email, phone, and color.
    
    Fields:
        color (CharField): HEX color associated with the contact.
        name (CharField): Name of the contact.
        email (EmailField): Email address of the contact.
        phone (CharField): Phone number of the contact.
    """
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    """
    Stores tasks with details including assigned contacts, due date, priority, and subtasks.
    
    Fields:
        task_title (CharField): Title of the task.
        description (TextField): Detailed description of the task.
        assigned_to (ManyToManyField): Contacts assigned to this task.
        due_date (DateField): Date by which the task should be completed.
        priority (CharField): Priority level of the task (e.g., urgent, medium).
        category (CharField): Category to which the task belongs.
        subtasks (JSONField): List of subtasks for the task.
        subtasks_done (JSONField): List of completed subtasks.
        state (CharField): Current state of the task (e.g., ToDo, InProgress, Done).
    """
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
