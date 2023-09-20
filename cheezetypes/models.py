from django.db import models

# Create your models here.

class Cheeze(models.Model):
    name = models.CharField(max_length=33)
    spice_level = models.IntegerField()

    class Meta:
        verbose_name_plural = 'cheezes'