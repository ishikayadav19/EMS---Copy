from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True)  # Automatically increments the empid
    empname = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField()
    
    def __str__(self):
        return f"{self.empname} ({self.empid})"
