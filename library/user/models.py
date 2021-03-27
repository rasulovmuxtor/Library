from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    phone = models.CharField(max_length=18)
    address = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name