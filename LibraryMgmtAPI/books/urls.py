from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'authors',AuthorViewSet)
router.register(r'ebooks',EbookViewSet)
router.register(r'bookusers',BookUserViewSet)
router.register(r'physical_books_public',PublicPhysicalBookViewSet)
router.register(r'physical_books',PhysicalBookViewSet)
router.register(r'physical_books_inventory',PhysicalBookInventoryViewSet)
urlpatterns = [
    path('',include(router.urls))
]

