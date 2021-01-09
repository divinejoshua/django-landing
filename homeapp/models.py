from django.db import models
from django.conf import settings


class Visitor(models.Model):
    ip 					    = models.CharField(max_length=50, null=True, blank=False)
    date 			        = models.DateTimeField(auto_now_add=True, verbose_name="date")
    location 			    = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.ip
