from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from gcharts import GChartsManager

class Contest(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

class Contestant(models.Model):
    user = models.ForeignKey(User)
    contest = models.ForeignKey(Contest)
    target_weight = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return "%s in %s contest" % (self.user, self.contest)

def gen_default_contestant():
        contestantList=Contestant.objects.all()
        if len(contestantList) > 0: return contestantList[0].id
        return None

class Weight(models.Model):    
    objects = GChartsManager()
    current_weight = models.IntegerField(default=0)
    current_date = models.DateTimeField(default=datetime.now)
    contestant = models.ForeignKey(Contestant,
    	unique_for_date="current_date",
    	default=gen_default_contestant)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.contestant.user) + ' weighed ' + str(self.current_weight) + ' on ' + self.current_date.strftime('%m/%d/%Y') 








