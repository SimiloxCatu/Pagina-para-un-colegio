from django.shortcuts import render,redirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)
from rest_framework import generics, permissions
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser, Student
from courses.models import Course  
from users.serializers import UserSerializer
from .forms import TeacherSignUpForm, StudentSignUpForm


def homepage(request):
    return render(request, 'home.html')


def home(request):
    if request.user.is_authenticated:
            return redirect('index')
    return render(request, 'registration/signup.html')


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            users = CustomUser.objects.all()
            data['html_user_list'] = render_to_string('user/includes/partial_user_list.html', {
                'users': users
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def user_create(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
    else:
        form = StudentSignUpForm()
    return save_user_form(request, form, 'user/includes/partial_user_create.html')


def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST, instance=user)
    else:
        form = StudentSignUpForm(instance=user)
    return save_user_form(request, form, 'user/includes/partial_user_update.html')


def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        users = CustomUser.objects.all()
        data['html_user_list'] = render_to_string('user/includes/partial_user_list.html', {
            'user': user
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('user/includes/partial_user_delete.html', context, request=request)
    return JsonResponse(data)


class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')