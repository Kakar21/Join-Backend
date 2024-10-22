from django.urls import path, include
from .views import TasksViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]