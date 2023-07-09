from django.db import models
import uuid

class Device(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField()
    check_out = models.BooleanField(default=False)
    belongs_to = models.ForeignKey('employee.Employee', on_delete=models.CASCADE,related_name='devices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Devices"
        ordering = ['name']
