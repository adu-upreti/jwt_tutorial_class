from rest_framework import viewsets,serializers
from .models import Book
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated

#get == list
#post == create
#put == update
#patch == partial_update

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']

class BookReadSerializer(serializers.ModelSerializer):
    author =  AuthorSerializer(read_only = True)
    class Meta:
        model = Book
        fields = ['id','name','price','author']

class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookViewsets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookReadSerializer

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return BookWriteSerializer
        return BookReadSerializer
    
    def get_queryset(self):
        user = self.request.user
        print(user, " token owner")
        return Book.objects.filter(author = user)