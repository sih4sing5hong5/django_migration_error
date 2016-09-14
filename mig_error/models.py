from django.db import models

# Create your models here.


class A(models.Model):
    data = models.CharField(max_length=30)


class B(models.Model):
    pass
