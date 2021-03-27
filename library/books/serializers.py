from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField()

    def get_available(self,obj):
        return obj.copies-obj.borrowing.count()

    class Meta:
        model = Book
        exclude = ('id', 'publisher','added_at','updated_at')
        read_only_fields = ('slug',)