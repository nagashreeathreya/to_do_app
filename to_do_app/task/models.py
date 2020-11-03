from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    status_choices = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    due_date = models.DateField()
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=status_choices, default='Pending')

    def __str__(self):
        return self.title
