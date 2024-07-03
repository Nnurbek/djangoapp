from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=255, unique=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255)
    file = models.FileField(upload_to='assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.course_name} - {self.student_id}"
