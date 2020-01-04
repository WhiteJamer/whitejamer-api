from django.db import models
from profiles.models import Profile


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.FileField(upload_to='portfolio/', null=True, blank=True)
    owner = models.ForeignKey(Profile, related_name='items', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
