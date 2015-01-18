from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.db import models
from gcharts import GChartsManager

# Create your models here.

def gen_default_contestant():
	userList=User.objects.all()
	if len(userList) > 0: return userList[0].id
	return None

class Weight(models.Model):
    objects = GChartsManager()
    current_weight = models.IntegerField(default=0)
    current_date = models.DateTimeField('date published', default=datetime.now)
    contestant = models.ForeignKey(settings.AUTH_USER_MODEL,
    	unique_for_date="current_date",
    	default=gen_default_contestant)
    def __str__(self):              # __unicode__ on Python 2
        return self.current_date.strftime('%m/%d/%Y')+ ' ' + str(self.current_weight)

class Contest(models.Model):
    contest_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.contest_name)

class Contestant(models.Model):
    user = models.ForeignKey(User)
    contest = models.ForeignKey(Contest)
    target_weight = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.user, self.contest)




