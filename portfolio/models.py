from django.db import models


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.FileField(upload_to='portfolio/', null=True, blank=True)

    def str(self):
        return self.title
