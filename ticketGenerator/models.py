from django.db import models
from django.utils import timezone

class Tambola(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    json_data = models.TextField()