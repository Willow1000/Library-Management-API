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
    class Meta:
        model = EBook
        fields="__all__"


class PhysicalBookSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model=PhysicalBookPublic
        fields = "__all__"

    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def ebook_available(self):
        return bool(EBook.objects.filter(title=self.title))

    def physical_book_available(self):
        return bool(PhysicalBookInventory.objects.get(title=self.title).stock_count())

class PhysicalBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhysicalBook      
        fields = "__all__"  

    def get_available(self, obj):
        return PhysicalBook.objects.filter(title=obj.title, author=obj.author).exists()

class PhysicalBookInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalBookInventory
        fields = "__all__"

    def stock_count(self):
        return PhysicalBook.objects.filter(title=self.title).count()   