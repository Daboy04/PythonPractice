from django.db import models

# Create your models here.
class Report(models.Model):
    user = models.CharField(max_length=250)
    report = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)