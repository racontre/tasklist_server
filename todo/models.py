from django.db import models

# Create your models here.
class Task (models.Model):
    name = models.CharField(max_length = 100)
    due_date = models.DateField()
    description = models.CharField(max_length = 1000, default = "")
    
    def __str__(self):
        return self.name