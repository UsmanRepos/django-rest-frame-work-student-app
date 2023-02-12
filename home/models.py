from django.db import models
    
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.first_name + " " + self.last_name

class Student(Person):
    major = models.CharField(max_length=100)
    gpa = models.FloatField()

    # def __str__(self):
    #     return f"{self.student_id}"
