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

    def __str__(self):
        return f'{self.id}: {self.title}'

    @property
    def summary(self):
        dots = '...' if len(self.content) > 100 else ''
        return f'{self.content[:100]}{dots}'

    @property
    def post_date_format(self):
        return self.post_date.strftime('%Y-%m-%d %H:%M')

    @property
    def edit_date_format(self):
        return self.edit_date.strftime('%Y-%m-%d %H:%M')
    

