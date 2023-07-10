from django.db import models
import uuid

class Device_Log(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4())
    device = models.ForeignKey('device.Device', on_delete=models.CASCADE,related_name='device',null=True,blank=True)
    working = models.BooleanField(default=True)
    belongs_to = models.ForeignKey('employee.Employee', on_delete=models.CASCADE,related_name='employee',null=True,blank=True)
    checked_out_date = models.DateTimeField(auto_now_add=True)
    checked_out_condition = models.CharField(max_length=50)
    returned_date = models.DateTimeField(auto_now_add=True)
    returened_condition = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.device.name
    class Meta:
        verbose_name_plural = "Device_Logs"
        ordering = ['device']
        