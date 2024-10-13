from django.shortcuts import render, redirect
from .models import Title, Tasks
from .forms import TitleForm, TasksForm, RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse# Create your views here.


def home(request):
    title = Title.objects.all
    tasks = Tasks.objects.all
    context = {
        'title': title,
        'tasks': tasks
    }
    return render(request, 'blog_app/index.html', context)


def crate_title(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
        else:
            form = TitleForm()

    form = TitleForm()
    context = {
        'form': form
    }
    return render(request, 'blog_app/create_title.html', context)


def create_tasks(request, pk):
    title = Title.objects.get(pk=pk)
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.category = title
            form.save()
            return redirect('home')
        else:
            form = TasksForm()

    form = TasksForm()
    context = {
        'form': form
    }
    return render(request, 'blog_app/create_tasks.html', context)


def delete_tasks(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    tasks.delete()
    return redirect(reverse('home'))


def delete_title(request, pk):
    title = Title.objects.get(pk=pk)
    title.delete()
    return redirect(reverse('home'))


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'blog_app/registration.html', context)


def login_(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'blog_app/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')
