from rest_framework import viewsets
from books.serializers import BookSerializer
from books.models import Book
from django.db.models import Count

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

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