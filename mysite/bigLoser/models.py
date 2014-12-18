from django.db import models

# Create your models here.


class Weight(models.Model):
    current_weight = models.IntegerField(default=0)
    current_date = models.DateTimeField('date published')


