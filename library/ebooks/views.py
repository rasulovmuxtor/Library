from rest_framework import viewsets
from .serializers import EbookSerializer
from ebooks.models import Ebook
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
