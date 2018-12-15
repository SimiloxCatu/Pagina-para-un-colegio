from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import CustomUser, Student
from courses.models import Course


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'telephone', 'is_student',  'is_teacher', 'is_supervisor')
        widgets = {
			'is_student': forms.Select(attrs={'class':'form-control'}),
			'is_teacher': forms.Select(attrs={'class':'form-control'}),
			'is_supervisor': forms.Select(attrs={'class':'form-control'}),
		}


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'telephone', 'is_student',  'is_teacher', 'is_supervisor')


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'telephone', 'is_student',  'is_teacher', 'is_supervisor')


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'telephone', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


'''class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'telephone')

    #@transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user'''


class StudentSignUpForm(UserCreationForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'telephone', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.courses.add(*self.cleaned_data.get('courses'))
        return user


class StudentCoursesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('courses', )
        widgets = {
            'courses': forms.CheckboxSelectMultiple
        }