from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission 
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    @property
    def books_written(self):
        return self.books.filter(author=self)
    # books_written = 

    def __str__(self):
        return self.name

class AbstractBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name = 'books')
    pages = models.IntegerField()
    publication_date = models.DateField()
    
    class Meta:
        abstract = True    

    def __str__(self):
        return self.title    


class PhysicalBook(AbstractBook):
    location = models.CharField(max_length=200)
    isbn = models.IntegerField(unique=True)
    available = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        Book.objects.get_or_create(title = self.title,author = self.author,physical_book_available=True,ebook_available=False)   
        PhysicalBookPublic.objects.get_or_create(title = self.title,pages=self.pages,author = self.author,publication_date = self.publication_date) 
            
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['isbn'],name='unique_isbn')
        ]
    def __str__(self):
        return self.title + "   " + self.author.name + "   " + str(self.isbn)    
class PhysicalBookPublic(AbstractBook):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name ='public_physical_books')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title','author'],name = 'public_physical_book_unique_title_author')
        ]    
class EBook(AbstractBook):
    size = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name = 'ebooks')
    file_format = models.CharField(max_length=50)
    download_link = models.URLField(max_length=200)
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        
        Book.objects.get_or_create(title = self.title,author = self.author,ebook_available=True,physical_book_available=False)    
            
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title','author'],name='unique_ebook_title_author')
        ]

class BookUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    member_no = models.AutoField(primary_key =True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return str(self.member_no)
class PhysicalBookInventory(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)
    location = models.CharField(max_length=50,blank=True)

class Book(models.Model):
    ebook_available = models.BooleanField()
    
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    physical_book_available=models.BooleanField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title','author'],name="unique_book_title_author")
        ]

class BookUserRecord(models.Model):
    STATUS_CHOICES = [
        ('Returned','returned'),
        ('Not Returned','not returned')
    ]
    user = models.ForeignKey(BookUser,on_delete=models.CASCADE)
    book = models.ForeignKey(PhysicalBook,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    borrowing_date = models.DateField()
    supposed_returning_date = models.DateField()
    returned_date = models.DateField()
    fine = models.PositiveIntegerField()      
     