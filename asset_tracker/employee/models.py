from django.db import models

# create a model for the employee
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Employees"
        ordering = ['name']
