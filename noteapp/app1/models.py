from django.db import models

# Create your models here.
class MyNotes(models.Model):
    title = models.CharField(max_length=50)
    data = models.CharField(max_length=1000)

    def __str__(self):
        return self.title