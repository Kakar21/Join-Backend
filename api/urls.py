from django.urls import path, include
from .views import TasksViewSet, ContactsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]