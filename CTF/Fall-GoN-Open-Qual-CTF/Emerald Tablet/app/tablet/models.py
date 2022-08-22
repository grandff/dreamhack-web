from django.db import models
import uuid


class Inscription(models.Model):
    inscriber = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    key = models.UUIDField(default=uuid.uuid4)

class Content(models.Model):
    data = models.TextField()
    inscription = models.OneToOneField(Inscription, models.CASCADE)
