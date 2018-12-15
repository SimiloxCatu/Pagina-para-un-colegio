from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from courses.models import Course

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('name', 'owner')
