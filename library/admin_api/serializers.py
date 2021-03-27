from ebooks.serializers import EbookSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import Student
from books.models import Book,Borrowing


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','last_login')


class EbookAdminSerializer(EbookSerializer):
    publisher = UserSerializer(read_only=True)

    class Meta(EbookSerializer.Meta):
        exclude = ('id',)
        read_only_fields = ('publisher','slug','added_at','updated_at')


class BookAdminSerializer(serializers.ModelSerializer):
    available = serializers.ReadOnlyField()
    class Meta:
        model = Book
        exclude = ('id',)
        read_only_fields = ('publisher','added_at','updated_at','slug')


class StudentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('id',)
        read_only_fields = ('student_id','created_at')


