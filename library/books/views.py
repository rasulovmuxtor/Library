from rest_framework import viewsets
from books.serializers import BookSerializer
from books.models import Book

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'