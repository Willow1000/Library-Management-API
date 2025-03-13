from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublicPhysicalBookViewSet(viewsets.ModelViewSet):
    queryset = PhysicalBookPublic.objects.all()
    serializer_class = PhysicalBookSerializerPublic

class EbookViewSet(viewsets.ModelViewSet):
    queryset = EBook.objects.all()
    serializer_class = EbookSerializer         

class BookUserViewSet(viewsets.ModelViewSet):
    queryset = BookUser.objects.all()
    serializer_class = BookUserSerializer       

class PhysicalBookViewSet(viewsets.ModelViewSet):
    queryset = PhysicalBook.objects.all()
    serializer_class = PhysicalBookSerializer    

class PhysicalBookInventoryViewSet(viewsets.ModelViewSet):
    queryset = PhysicalBookInventory.objects.all()
    serializer_class = PhysicalBookInventorySerializer    

class BookUserRecordViewset(viewsets.ModelViewSet):
    queryset = BookUserRecord.objects.all()
    serializer_class = BookUserRecordSerializer    