from django.db import models
import uuid

class Company(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    ceo = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

