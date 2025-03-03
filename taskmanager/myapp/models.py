from django.db import models

# Create your models here.
class Task(models.Model):  
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Due Today', 'Due Today'),
        ('Overdue', 'Overdue')
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')
    
    def __str__(self):
        return self.title