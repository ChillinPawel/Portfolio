from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.title}'