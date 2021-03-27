from ebooks.serializers import EbookSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','last_login')

class EbookAdminSerializer(EbookSerializer):
    publisher = UserSerializer(read_only=True)
    class Meta(EbookSerializer.Meta):
        exclude = ('id',)
        read_only_fields = ('publisher','slug','added_at','updated_at')