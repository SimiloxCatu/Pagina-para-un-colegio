from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Course, Homework
from .forms import CourseForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def save_course_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            courses = Course.objects.all()
            data['html_course_list'] = render_to_string('courses/includes/partial_course_list.html', {
                'courses': courses
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
    else:
        form = CourseForm()
    return save_course_form(request, form, 'courses/includes/partial_course_create.html')


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
    else:
        form = CourseForm(instance=course)
    return save_course_form(request, form, 'courses/includes/partial_course_update.html')


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    data = dict()
    if request.method == 'POST':
        course.delete()
        data['form_is_valid'] = True
        courses = Course.objects.all()
        data['html_course_list'] = render_to_string('courses/includes/partial_course_list.html', {
            'course': course
        })
    else:
        context = {'course': course}
        data['html_form'] = render_to_string('courses/includes/partial_course_delete.html', context, request=request)
    return JsonResponse(data)