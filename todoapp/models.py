from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    kurs = models.PositiveSmallIntegerField()
    s_raqam = models.PositiveSmallIntegerField( unique=True, default=0 )
    def __str__(self):
        return self.ism
class Project(models.Model):
    sarlovha = models.CharField(max_length=50)
    reja = models.TextField(blank=True)
    sana = models.DateField()
    bajarilgan = models.BooleanField()
    student = models.ForeignKey(Student,  on_delete=models.CASCADE, related_name="m_student")
    def __str__(self):
        return self.sarlovha