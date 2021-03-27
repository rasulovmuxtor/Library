from rest_framework import viewsets
from ebooks.serializers import EbookSerializer
from ebooks.models import Ebook

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

class EbookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    lookup_field = 'slug'

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            "E-Books root Endpoints":reverse('ebooks:api-root', request=request, format=format),
            "Books root Endpoints":reverse('books:api-root', request=request, format=format),
            "Admin root Endpoints":reverse('admin-api:api-root', request=request, format=format),
            'Post the username and password to create token for a user': reverse('user:token_auth', request=request, format=format),
            "Change password": reverse('user:change-password', request=request, format=format)
            })