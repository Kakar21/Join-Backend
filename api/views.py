from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Task, Contact
from .serializers import TaskSerializer, ContactSerializer, SummarySerializer


class TasksViewSet(viewsets.ModelViewSet):
    """CRUD operations for tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ContactsViewSet(viewsets.ModelViewSet):
    """CRUD operations for contacts, ordered by name."""
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer


class SummaryView(APIView):
    """Provides task summary counts by state and priority."""
    def get(self, request):
        todo_count = Task.objects.filter(state="ToDo").count()
        done_count = Task.objects.filter(state="Done").count()
        urgent_count = Task.objects.filter(priority="urgent").count()
        tasks_count = Task.objects.all().count()
        in_progress_count = Task.objects.filter(state="InProgress").count()
        awaiting_feedback_count = Task.objects.filter(
            state="AwaitFeedback").count()

        summary = {
            "todo_count": todo_count,
            "done_count": done_count,
            "urgent_count": urgent_count,
            "tasks_count": tasks_count,
            "in_progress_count": in_progress_count,
            "awaiting_feedback_count": awaiting_feedback_count
        }
        serializer = SummarySerializer(summary)
        return Response(serializer.data)
