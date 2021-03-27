from django.db import models
from ebooks.models import AbstractBook
from user.models import Student

class Book(AbstractBook):
    copies = models.PositiveSmallIntegerField()


class Borrowing(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowing')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='borrowing')
    returned = models.BooleanField(default=False)
    until_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def clean(self):
        if self.book.copies-self.book.borrowing.filter(returned=False).count()==0:
            raise ValidationError(_('The book not available'))


    def __str__(self):
        return f"{self.student} - {self.book}"