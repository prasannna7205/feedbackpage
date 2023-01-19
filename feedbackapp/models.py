from django.db import models

class UserComment (models.Model):
    commment = models.CharField(max_length=100)
