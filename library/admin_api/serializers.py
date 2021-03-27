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
    publisher = UserSerializer(read_only=True)
    available = serializers.SerializerMethodField()

    def get_available(self,obj):
        return obj.copies-obj.borrowing.count()
    class Meta:
        model = Book
        exclude = ('id',)
        read_only_fields = ('publisher','added_at','updated_at','slug')

class RelatedBookSerializer(serializers.ModelSerializer):
    available = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = ('author','title','copies','available','slug')


class RelatedBorrowingSerializer(serializers.ModelSerializer):
    book = RelatedBookSerializer(read_only=True)
    class Meta:
        model = Borrowing
        exclude = ('student',)


class StudentAdminSerializer(serializers.ModelSerializer):
    borrowed_books = RelatedBorrowingSerializer(many=True,source='borrowing',required=False)
    class Meta:
        model = Student
        exclude = ('id',)
        read_only_fields = ('created_at','borrowed_books')

class RelatedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('id',)
        read_only_fields = ('student_id','created_at')

class BorrowingAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['book'] = RelatedBookSerializer(instance=instance.book).data
        representation['student'] = RelatedStudentSerializer(instance=instance.student).data
        
        return representation

