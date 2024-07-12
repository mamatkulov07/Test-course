from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    phone_number = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=[('teacher', 'Teacher'), ('student', 'Student')], default='student')

    def str(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    instructor_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    level = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    level = models.CharField(max_length=100, choices=level)


class Module(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Lesson(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.DateTimeField()
    video_url = models.FileField(upload_to='file/')
    duration = models.DateTimeField()


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField()
    progress = models.TextField()


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='file/')
    submitted = models.DateTimeField()


class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(default=0)
    feedback = models.DateTimeField()


class Certificate(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.CharField(max_length=100)


