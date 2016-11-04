from django.db import models
from django.utils import timezone
import datetime

class Wpis(models.Model):
    author = models.ForeignKey('auth.User')
    weight = models.DecimalField(max_digits = 3, decimal_places = 1, blank=True, null=True)
    belt = models.DecimalField(max_digits = 3, decimal_places = 1, blank=True ,null=True)
    waist = models.DecimalField(max_digits = 3, decimal_places = 1, blank=True, null=True)
    created_date = models.DateTimeField()
    
    def __str__(self):
        return str(self.created_date)