from django.urls import path, include
from .views import TasksViewSet, ContactsViewSet, SummaryView
from rest_framework import routers

# Register ViewSets with the router
router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)), # Includes task and contact routes
    path('summary/', SummaryView.as_view()), # Provides summary data for tasks
]