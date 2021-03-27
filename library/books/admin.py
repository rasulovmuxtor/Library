from django.contrib import admin

from books.models import Book,Borrowing

admin.site.register(Book)
admin.site.register(Borrowing)