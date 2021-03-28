from books.models import Book, Borrowing
from ebooks.models import Ebook
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from user.models import Student

from admin_api.serializers import (BookAdminSerializer,
                                   BorrowingAdminSerializer,
                                   EbookAdminSerializer,
                                   StudentAdminSerializer)


class EbookAdminViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

    def get_queryset(self):
        queryset = Ebook.objects.all()
        author = self.request.query_params.get('author')
        language = self.request.query_params.get('language')
        author = self.request.query_params.get('author')
        publication_year = self.request.query_params.get('publication_year')
        
        if author is not None:
            queryset = queryset.filter(author=author)
        if language is not None:
            queryset = queryset.filter(language=language)
        if publication_year is not None:
            queryset = queryset.filter(publication_date__year=publication_year)
        return queryset

class BookAdminViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
    
    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        language = self.request.query_params.get('language')
        author = self.request.query_params.get('author')
        publication_year = self.request.query_params.get('publication_year')
        
        if author is not None:
            queryset = queryset.filter(author=author)
        if language is not None:
            queryset = queryset.filter(language=language)
        if publication_year is not None:
            queryset = queryset.filter(publication_date__year=publication_year)
        return queryset

class StudentAdminViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'student_id'
    
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__search=name)



class BorrowingAdminViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingAdminSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Borrowing.objects.all()
        booktitle = self.request.query_params.get('booktitle')
        returned = self.request.query_params.get('returned')
        if booktitle is not None:
            queryset = queryset.filter(book__title__search=booktitle)
        if returned == 'true':
            queryset = queryset.filter(returned=True)
        elif returned == 'false':
            queryset = queryset.filter(returned=False)
        return queryset