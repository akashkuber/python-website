from django.db import models


class AllCourses(models.Model):
    courseName = models.CharField(max_length=200)
    insName = models.CharField(max_length=100)


class Details(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)
