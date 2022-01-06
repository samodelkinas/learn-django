from django.db import models
from sorl.thumbnail import ImageField


class Student(models.Model):
    first_name = models.CharField(max_length=140, blank=False, null=False)
    last_name = models.CharField(max_length=140, blank=False, null=False)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Question(models.Model):
    text = models.CharField(max_length=2000, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return f"{self.text}"
