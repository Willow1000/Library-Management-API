from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUser
        fields = '__all__'

class EbookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.name',read_only=True)
    class Meta:
        model = EBook
        fields="__all__"


class PhysicalBookSerializerPublic(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.name',read_only=True)
    class Meta:
        model=PhysicalBookPublic
        fields = "__all__"

    

class BookSerializer(serializers.ModelSerializer ):
     
    ebook_available = serializers.BooleanField(read_only=True)
    physical_book_available = serializers.BooleanField(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"
        
    

class PhysicalBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhysicalBook      
        fields = "__all__"  

class PhysicalBookInventorySerializer(serializers.ModelSerializer):
    stock_count = serializers.IntegerField(read_only=True,default = PhysicalBook.objects.all().count())
    class Meta:
        model = PhysicalBookInventory
        exclude = ['location']
    
    
class BookUserRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookUserRecord
        fields = '__all__'    