from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import LoginForm, AddTaskForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Task
from datetime import date
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm})

    def post(self, request):
        user = authenticate(email=str(request.POST['email']), password=str(request.POST['password']))
        if user is not None:
            return render(request, 'home.html', {'user': user.email, 'form': AddTaskForm})
        else:
            user = User.objects.create_user(username=str(request.POST['email']), email=str(request.POST['email']),
                                                           password=str(request.POST['password']))
            user.save()
            return render(request, 'home.html', {'user': user.email, 'form': AddTaskForm})


class TasksView(View):
    def get(self, request):
        task = Task.objects.all()
        return render(request, 'home.html', {'form': AddTaskForm, 'task': task, 'show_table': 'Yes'})


    def post(self, request):
        task_dict = {}
        d = request.POST['due_date'].split('/')
        get_user = User.objects.get(email=request.POST['user'])
        task_dict['user'] = get_user
        task_dict['title'] = request.POST['title']
        task_dict['due_date'] = date(int(d[2]), int(d[0]), int(d[1]))
        task_dict['category'] = request.POST['category']
        task_dict['status'] = request.POST['status']

        task = Task(**task_dict)
        task.save()

        return render(request, 'home.html', {'form': AddTaskForm, 'show_table': 'No'})



