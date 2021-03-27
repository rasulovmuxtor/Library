from rest_framework import viewsets
from ebooks.serializers import EbookSerializer
from ebooks.models import Ebook

class EbookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    lookup_field = 'slug'
