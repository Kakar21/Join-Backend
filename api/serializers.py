from rest_framework import serializers
from .models import Task, Contact
from datetime import date


class ContactSerializer(serializers.ModelSerializer):
    """Serializes all fields for the Contact model."""
    class Meta:
        model = Contact
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """Serializes task data with related contacts and subtasks."""
    assigned_to = ContactSerializer(many=True, read_only=True)
    contact_ids = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        many=True,
        write_only=True,
        source="assigned_to",
        required=False
    )
    subtasks = serializers.ListField(
        child=serializers.CharField(), required=False)
    subtasks_done = serializers.ListField(
        child=serializers.CharField(), required=False)

    class Meta:
        model = Task
        fields = ["id", "task_title", "description", "contact_ids", "assigned_to",
                  "due_date", "priority", "category", "subtasks", "subtasks_done", "state"]


class SummarySerializer(serializers.Serializer):
    """Serializes summary data including task counts and next deadline."""
    todo_count = serializers.IntegerField()
    done_count = serializers.IntegerField()
    urgent_count = serializers.IntegerField()
    next_deadline = serializers.SerializerMethodField()
    tasks_count = serializers.IntegerField()
    in_progress_count = serializers.IntegerField()
    awaiting_feedback_count = serializers.IntegerField()

    def get_next_deadline(self, obj):
        """
        Returns the date of the next upcoming task deadline.
        """
        task_dates_sorted = Task.objects.order_by("due_date")
        for task in task_dates_sorted:
            if task.due_date <= date.today():
                continue
            else:
                deadline = task.due_date.strftime('%B %d, %Y')
                return deadline
