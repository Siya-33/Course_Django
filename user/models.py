from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20,null=True, blank=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=2,null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11,null=True, blank=True)


class Course(models.Model):
    cno= models.AutoField(primary_key=True)
    cname=models.CharField(max_length=20)
    ccredit=models.DecimalField(max_digits=2, decimal_places=1)
    cteacher=models.CharField(max_length=20)
    cdeptno=models.CharField(null=True,max_length=20)
    cmax_number = models.IntegerField(null=True,verbose_name="课程最大人数")

class SC(models.Model):
    sno = models.ForeignKey(Student, on_delete=models.PROTECT)
    cno = models.ForeignKey(Course, on_delete=models.PROTECT)
    status = models.IntegerField(default=1)    #状态


