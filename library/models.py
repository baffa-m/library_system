from django.db import models
from datetime import datetime
import uuid
# Create your models here.
    

class Categories(models.Model):
    category = models.CharField(max_length=200, unique=True, null=False)
    
    def __st__(self):
        return f"{self.name}"
    
class Books(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField()
    date_received = models.DateTimeField(default=datetime.utcnow)
    
    
    def __st__(self):
        return f"{self.tilte} by {self.author}"
    
    
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Books, on_delete=models.RESTRICT)
    due_back = models.DateField(null=True)
    
    catchchoices = (
        ("m", "maintenance"),
        ("r", "Reserved"),
        ("c", "Checked Out"),
        ("a", "Available")
    )
    
    status = models.CharField(max_length=1, choices=catchchoices, default="a")
    
    def __str__(self):
        return f"{self.title}, {self.book.title}"   
    
    class Meta:
        ordering = ["due_back"]