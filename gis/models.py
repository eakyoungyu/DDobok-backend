from django.db import models

# class Photo(models.Model):

#     """Photo Model Definition"""

#     caption = models.CharField(max_length=50)
#     file = models.ImageField(upload_to="gi_photos")
#     gi = models.ForeignKey("Gi", related_name="photos", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.caption


class Gi(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 0
        MID = 1
        HIGH = 3
        COMMERCIAL = 4

    class Color(models.TextChoices):
        BLACK = "Black"
        WHITE = "White"
        BLUE = "Blue"
        BRIGHT = "Bright"
        DARK = "Dark"

    """Gi Model Definition"""

    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        "brands.Brand", related_name="gis", on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to="gi_photos")
    link_store = models.URLField()
    price = models.IntegerField()
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)

    color = models.CharField(choices=Color.choices, max_length=15)

    def __str__(self):
        return self.name
