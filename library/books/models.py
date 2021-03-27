from django.db import models
from ebooks.models import AbstractBook
from user.models import Student

class Book(AbstractBook):
    copies = models.PositiveSmallIntegerField()

    @property
    def available(self):
        return self.copies-self.borrowing.count()


class Borrowing(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowing')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='borrowing')
    returned = models.BooleanField(default=False)
    until_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student} - {self.book}"