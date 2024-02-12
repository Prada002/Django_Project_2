from django.db import models

# Create your models here.
class Depart(models.Model):
    dept = models.CharField(max_length=255)



class DataList(models.Model):
    name = models.CharField(max_length=255, default=None)
    roll_no = models.CharField(max_length=20)
    email = models.EmailField()
    dept = models.ForeignKey(Depart, on_delete=models.CASCADE, null=True)