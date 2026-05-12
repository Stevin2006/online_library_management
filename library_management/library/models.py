from django.db import models

from books.models import Book
from student.models import Student


class Library(models.Model):
      student = models.ForeignKey(Student, on_delete=models.CASCADE)

      book = models.ForeignKey(Book, on_delete=models.CASCADE)
      lending_date = models.DateTimeField(auto_now_add=True)
      exp_return_date = models.DateField()
      return_date = models.DateField(null=True , blank=True)
      def __str__(self):
            return f'{self.student.first_name} {self.student.last_name} {self.book.title}'
