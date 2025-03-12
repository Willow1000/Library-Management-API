from django.db import models

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
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')
    isbn = models.IntegerField(unique=True)
    available = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        Book.objects.get_or_create(title = self.title,author = self.author)   
        PhysicalBookPublic.objects.get_or_create(title = self.title,pages=self.pages,author = self.author,publication_date = self.publication_date) 
            
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['isbn'],name='unique_isbn')
        ]
class PhysicalBookPublic(AbstractBook):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name ='public_physical_books')
    @property
    def available(self):
        return bool(PhysicalBook.objects.filter(title = self.title,author=self.author))
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
        
        Book.objects.get_or_create(title = self.title,author = self.author)    
            
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title','author'],name='unique_ebook_title_author')
        ]

class BookUser(models.Model):
    name = models.CharField(max_length=200)
    member_no = models.AutoField(primary_key =True)
    
    
class PhysicalBookInventory(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    @property
    def stock_count(self):
        return PhysicalBook.objects.filter(title=self.title).count()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    @property
    def ebook_available(self):
        return bool(EBook.objects.filter(title=self.title))

    @property
    def physical_book_available(self):
        return bool(PhysicalBookInventory.objects.get(title=self.title).stock_count())

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title','author'],name="unique_book_title_author")
        ]