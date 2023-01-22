from django.db import models


class Brand(models.Model):

    """Brand Model Definition"""

    name = models.CharField(max_length=20)
    link_store = models.URLField()
    link_sns = models.URLField()

    def __str__(self):
        return self.name
