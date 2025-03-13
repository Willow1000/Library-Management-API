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
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            title = self.data['title']
            author = self.data['author']
            self.fields['ebook_available'].default = EBook.objects.filter(title=title,author = author).exists()
            self.fields['physical_book_available'].default = PhysicalBookPublic.objects.filter(title=title,author = author).exists()

        
    

class PhysicalBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhysicalBook      
        fields = "__all__"  

    def get_available(self, obj):
        return PhysicalBook.objects.filter(title=obj.title, author=obj.author).exists()

class PhysicalBookInventorySerializer(serializers.ModelSerializer):
    stock_count = serializers.IntegerField(read_only=True,default = PhysicalBook.objects.all().count())
    class Meta:
        model = PhysicalBookInventory
        exclude = ['location']
    
    
class BookUserRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookUserRecord
        fields = '__all__'    