from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100 , choices=(('Male','Male'),('Female','Female')) , default='Male')
    reg_number = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

