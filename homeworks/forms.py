from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from courses.models import Homework, Assistance

class HomeworkForm(forms.ModelForm):

	class Meta:
		model = Homework
		fields = ('title', 'text', 'course', 'created_date', 'delivery_date')