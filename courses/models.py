from django.db import models
from users.models import CustomUser, Student
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Homework(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.create_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


class Assistance(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    students = models.ManyToManyField(Student, related_name='assistance_students')

    def publish(self):
        self.create_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.date