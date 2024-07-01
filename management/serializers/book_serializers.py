from rest_framework import serializers
from ..models import Book

class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'