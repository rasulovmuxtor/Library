from ebooks.models import Ebook
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admin_api.serializers import EbookAdminSerializer, StudentAdminSerializer, BookAdminSerializer
from books.models import Book,Borrowing
from user.models import Student


class EbookAdminViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class BookAdminViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class StudentAdminViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'student_id'