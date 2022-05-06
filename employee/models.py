from django.db import models

# Create your models here.

class employees(models.Model):
    emp_name=models.CharField(max_length=120)
    dept = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    salary= models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.email

# ORM queries
#
#  CRUD Oprations
# create
# orm queries for creating a new employee
#     emp=employees(emp_name="abc",dept="abc",email="abc@gamil.com", salary=50000,experience=5)
#     emp.save()
# retrieve
# orm queries for listing all employees
# emp=employees.objects.all()
# emp

# orm filtering
# orm query for listing all employees whose dept is IT.
# emp=employees.objects.filter(dept="IT")
# emp

# orm query for listing al  l employees whose experience greater than 2.
# emp=employees.objects.filter(experience__gt=2)
# emp

# orm query for listing all employees whose salary greater than 20000
# emp=employees.objects.filter(salary__gt=20000)
# emp

# orm query for listing all employees whose salary less than 20000
# emp=employees.objects.filter(salary__lt=20000)
# emp

# orm query for listing all employees whose salary is greater than or equal to 30000
# emp=employees.objects.filter(salary__gte=30000)
# emp

# orm query for listing all employees whose salary is greater than 10000 but less than 30000
# emp=employees.objects.filter(salary__gt=10000,salary__lt=30000)
# emp

# orm query for listing all employees whose salary is greater than or equal to 20000 but less than 30000
# emp=employees.objects.filter(salary__gte=20000,salary__lt=30000)
# emp

# Fetching a specific object
# orm query for fetching a specific record using its id

# emp=employees.objects.get(id=3)
# emp

# update
# delete