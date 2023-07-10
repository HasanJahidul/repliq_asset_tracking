from django.db import models
import uuid

# create a model for the employee
class Employee(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='employees')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Employees"
        ordering = ['name']
