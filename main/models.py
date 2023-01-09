from django.db import models

# Create your models here.

class GalleryModel(models.Model):
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.desc

