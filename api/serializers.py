from rest_framework import serializers
from .models import Task, Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = ContactSerializer(many=True, read_only=True)
    contact_ids = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        many=True,
        write_only=True,
        source="assigned_to",
    )
    subtasks = serializers.ListField(
        child=serializers.CharField(), required=False)
    subtasks_done = serializers.ListField(
        child=serializers.CharField(), required=False)

    class Meta:
        model = Task
        fields = ["id", "task_title", "description", "contact_ids", "assigned_to",
                  "due_date", "priority", "category", "subtasks", "subtasks_done", "state"]


class SummarySerializer(serializers.ModelSerializer):
    pass