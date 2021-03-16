from django.db import models
from django.utils import timezone

class Comment(models.Model):
    user = models.CharField(max_length=50)
    post_date = models.DateTimeField(editable=False)
    content = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''

        if not self.id:
            self.post_date = timezone.now()
        return super(Comment, self).save(*args, *kwargs)

    def __str__(self):
        return f'{self.id}: {self.user} - {self.short_summary}'

    @property
    def short_summary(self):
        dots = '...' if len(self.content) > 30 else ''
        return f'{self.content[:30]}{dots}'

    @property
    def summary(self):
        dots = '...' if len(self.content) > 100 else ''
        return f'{self.content[:100]}{dots}'

    @property
    def post_date_format(self):
        return self.post_date.strftime('%Y-%m-%d %H:%M')
