from ebooks.models import Ebook
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admin_api.serializers import EbookAdminSerializer


class EbookAdminViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookAdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
