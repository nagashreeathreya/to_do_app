from django.urls import path, include
from task.views import LoginView, TasksView

urlpatterns = [
    path('', LoginView.as_view()),
    path('home/', LoginView.as_view()),
    path('addtasks/', TasksView.as_view()),
    path('viewtasks/', TasksView.as_view())
]
