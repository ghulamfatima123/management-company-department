from django.db import models

class Company(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=255)

    def __str__(self):
        return self.com_name

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)
    com_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name
