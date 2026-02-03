from django.db import models

# Create your models here.

class Learn_rset(models.Model):
    teacher_name = models.CharField(max_length=30)
    course_name = models.CharField(max_length=20)
    course_duration = models.IntegerField()
    seat = models.IntegerField()

