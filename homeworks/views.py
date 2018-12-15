from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from courses.models import Course, Homework
from .forms import HomeworkForm


def homework_list(request):
    homeworks = Homework.objects.all()
    return render(request, 'homeworks/homework_list.html', {'homeworks': homeworks})


def save_homework_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            homeworks = Homework.objects.all()
            data['html_homework_list'] = render_to_string('homeworks/includes/partial_homework_list.html', {
                'homeworks': homeworks
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def homework_create(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
    else:
        form = HomeworkForm()
    return save_homework_form(request, form, 'homeworks/includes/partial_homework_create.html')


def homework_update(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
    else:
        form = HomeworkForm(instance=homework)
    return save_homework_form(request, form, 'homeworks/includes/partial_homework_update.html')


def homework_delete(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    data = dict()
    if request.method == 'POST':
        homework.delete()
        data['form_is_valid'] = True
        homeworks = Homework.objects.all()
        data['html_homework_list'] = render_to_string('homeworks/includes/partial_homework_list.html', {
            'homework': homework
        })
    else:
        context = {'homework': homework}
        data['html_form'] = render_to_string('homeworks/includes/partial_homework_delete.html', context, request=request)
    return JsonResponse(data)