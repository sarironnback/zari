from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Creation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="creation")
    description = RichTextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class About(models.Model):
    edited_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="profile")
    description = RichTextField()
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.email