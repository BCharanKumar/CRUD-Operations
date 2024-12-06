from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, null = False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position

class Employee (models.Model):
    emp_first_name = models.CharField(max_length=100)
    emp_last_name = models. CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary= models. IntegerField()
    bonus =models. IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone= models. IntegerField(default=0)
    hire_date =models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.emp_first_name, self.emp_last_name, self.role)
