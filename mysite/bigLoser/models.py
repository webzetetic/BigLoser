from django.db import models

# Create your models here.


class Weight(models.Model):
    current_weight = models.IntegerField(default=0)
    current_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.current_date.strftime('%m/%d/%Y')+ ' ' + str(self.current_weight)


