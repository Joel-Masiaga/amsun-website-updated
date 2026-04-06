from django.db import models

# Create your models here.
class Events(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('cultural', 'Cultural'),
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='events_pics/', blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
    
class News(models.Model):
    CATEGORY_CHOICES = [
        ('announcement', 'Announcement'),
        ('achievement', 'Achievement'),
        ('academic', 'Academic'),
        ('research', 'Research'),
        ('partnership', 'Partnership'),
        ('innovation', 'Innovation'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]
    
    headline = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    author = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='news_pics/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.headline
    
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('research', 'Research'),
        ('healthTech', 'Health Tech'),
        ('education', 'Education'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
        ('science', 'Science'),
        ('finance', 'Finance'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
    