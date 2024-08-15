from django.db import models

# Create your models here.

class Teacher(models.Model):
    teach_name=models.CharField(max_length=50)
    teach_id=models.IntegerField()
    def __str__(self):
        return self.teach_name


class Subject(models.Model):
    sub_code=models.IntegerField()
    sub_name=models.CharField(max_length=50)
    teach_name=models.ForeignKey(Teacher,on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.sub_name




class Course(models.Model):
    course_name=models.CharField(max_length=50)
    course_desc=models.CharField(max_length=50)
    reg_date=models.DateTimeField()

    def __str__(self):
        return self.course_name
    
class stu_register_course(models.Model):
    stu_name=models.CharField(max_length=50)
    course_name=models.ManyToManyField(Course)

    def __str__(self):
        return self.stu_name





class Enroll(models.Model):
    stu_enrollment=models.IntegerField()
    enroll_by=models.CharField(max_length=50)

    def __str__(self):
        return str(self.stu_enrollment)
    
    
    class Meta:
       verbose_name_plural='Enroll'
    
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_enrollment=models.OneToOneField(Enroll,on_delete=models.CASCADE)

    def __str__(self):
        return self.stu_name    
    

    class Meta:
        verbose_name_plural='Student'

        