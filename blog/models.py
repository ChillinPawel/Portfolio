from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField(editable=False)
    edit_date = models.DateTimeField(editable=False)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''

        if not self.id:
            self.post_date = timezone.now()
        self.edit_date = timezone.now()
        return super(Blog, self).save(*args, *kwargs)
