from rest_framework import serializers
from.models import Task, Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subtask
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    assignedTo = SubtaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"