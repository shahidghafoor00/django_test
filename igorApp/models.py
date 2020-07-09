from django.db import models


class Test(models.Model):
    sample_field = models.CharField(max_length=200)