from django.urls import path, include
from .views import TasksViewSet, ContactsViewSet, SummaryView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', SummaryView.as_view()),
]