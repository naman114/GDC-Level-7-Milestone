"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import (
    GenericTaskView,
    GenericTaskCreateView,
    GenericTaskUpdateView,
    GenericTaskDetailView,
    GenericTaskDeleteView,
    session_storage_view,
    UserCreateView,
    UserLoginView,
    GenericCompletedTaskView,
    GenericMarkTaskAsCompleteView,
    GenericAllTaskView,
)
from django.contrib.auth.views import LogoutView

from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter
from tasks.apiviews import TaskListAPI, TaskViewSet, TaskHistoryViewSet


router = SimpleRouter()
router.register("api/task", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("all_tasks/", GenericAllTaskView.as_view()),
    path("", RedirectView.as_view(url="/tasks")),
    path("tasks/", GenericTaskView.as_view()),
    path("completed_tasks/", GenericCompletedTaskView.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("update-task/<pk>/", GenericTaskUpdateView.as_view()),
    path("detail-task/<pk>/", GenericTaskDetailView.as_view()),
    path("delete-task/<pk>/", GenericTaskDeleteView.as_view()),
    path("complete_task/<pk>/", GenericMarkTaskAsCompleteView.as_view()),
    path("user/signup/", UserCreateView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("sessiontest/", session_storage_view),
    path("taskapi/", TaskListAPI.as_view()),
    path("api/task/history/<id>/", TaskHistoryViewSet.as_view({"get": "list"})),
] + router.urls
