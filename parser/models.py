from django.db import models


class ParserModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parser/', null=True)

    def __str__(self):
        return self.title
