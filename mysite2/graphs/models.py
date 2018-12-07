from django.db import models

# Create your models here.
class perDayData(models.Model):
    day = models.DateTimeField()
    DailyVar = models.IntegerField()