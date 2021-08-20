from django.db import models
from django.utils import timezone
from django.urls import reverse

class Quiz(models.Model):
    BAT_CHOICE = {
        ("B.Tech 20" , "B.Tech 20"),
        ("B.Tech 19" , "B.Tech 19"),
        ("B.Tech 18" , "B.Tech 18"),
        ("B.Tech 17" , "B.Tech 17"),
        ("B.Tech 16" , "B.Tech 16"),
        ("B.Des 20" , "B.Des 20"),
        ("B.Des 19" , "B.Des 19"),
        ("B.Des 18" , "B.Des 18"),
        ("B.Des 17" , "B.Des 17"),
        ("B.Des 16" , "B.Des 16"),
        ("M.Tech 20" , "M.Tech 20"),
        ("M.Tech 19" , "M.Tech 19"),
        ("M.Tech 18" , "M.Tech 18"),
        ("M.Tech 17" , "M.Tech 17"),
        ("M.Tech 16" , "M.Tech 16"),
        ("PhD 20" , "PhD 20"),
        ("PhD 19" , "PhD 19"),
        ("PhD 18" , "PhD 18"),
        ("PhD 17" , "PhD 17"),
        ("PhD 16" , "PhD 16"),
    }
    DEP_CHOICE ={
        ("Computer Science and Engineering","Computer Science and Engineering"),
        ("Biosciences and Bioengineering","Biosciences and Bioengineering"),
        ("Chemical Engineering","Chemical Engineering"),
        ("Civil Engineering","Civil Engineering"),
        ("Chemimal Science and Technology","Chemimal Science and Technology"),
        ("Design","Design"),
        ("Electronics and Electrical Engineering","Electronics and Electrical Engineering"),
        ("Mechanical Engineering","Mechanical Engineering"),
        ("Electronics and Communications Engineering","Electronics and Communications Engineering"),
        ("Mathematics and Computing","Mathematics and Computing"),
        ("Engineering Physics","Engineering Physics"),
        ("Humanities and Social Sciences","Humanities and Social Sciences"),
    }
    batch = models.CharField(max_length=13,choices = BAT_CHOICE)
    department = models.CharField(max_length=50,choices = DEP_CHOICE)
    section = models.CharField(max_length=1,default='0')
    course = models.CharField(max_length=5,default="none")
    title = models.CharField(max_length=20,default="quiz title")
    description = models.TextField()
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    
    class Meta:
        ordering = ('date',)
    
    def __str__(self):
        if self.section=='0':
            return f'{self.title}, {self.course}'
        else:
            return f'{self.title}, {self.course} for Section:{self.section}'

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={"pk": self.pk})

class Assignment(models.Model):
    BAT_CHOICE = {
        ("B.Tech 20" , "B.Tech 20"),
        ("B.Tech 19" , "B.Tech 19"),
        ("B.Tech 18" , "B.Tech 18"),
        ("B.Tech 17" , "B.Tech 17"),
        ("B.Tech 16" , "B.Tech 16"),
        ("B.Des 20" , "B.Des 20"),
        ("B.Des 19" , "B.Des 19"),
        ("B.Des 18" , "B.Des 18"),
        ("B.Des 17" , "B.Des 17"),
        ("B.Des 16" , "B.Des 16"),
        ("M.Tech 20" , "M.Tech 20"),
        ("M.Tech 19" , "M.Tech 19"),
        ("M.Tech 18" , "M.Tech 18"),
        ("M.Tech 17" , "M.Tech 17"),
        ("M.Tech 16" , "M.Tech 16"),
        ("PhD 20" , "PhD 20"),
        ("PhD 19" , "PhD 19"),
        ("PhD 18" , "PhD 18"),
        ("PhD 17" , "PhD 17"),
        ("PhD 16" , "PhD 16"),
    }
    DEP_CHOICE ={
        ("Computer Science and Engineering","Computer Science and Engineering"),
        ("Biosciences and Bioengineering","Biosciences and Bioengineering"),
        ("Chemical Engineering","Chemical Engineering"),
        ("Civil Engineering","Civil Engineering"),
        ("Chemimal Science and Technology","Chemimal Science and Technology"),
        ("Design","Design"),
        ("Electronics and Electrical Engineering","Electronics and Electrical Engineering"),
        ("Mechanical Engineering","Mechanical Engineering"),
        ("Electronics and Communications Engineering","Electronics and Communications Engineering"),
        ("Mathematics and Computing","Mathematics and Computing"),
        ("Engineering Physics","Engineering Physics"),
        ("Humanities and Social Sciences","Humanities and Social Sciences"),
    }
    batch = models.CharField(max_length=13,choices = BAT_CHOICE)
    department = models.CharField(max_length=50,choices = DEP_CHOICE)
    section = models.CharField(max_length=1,default='0')
    course = models.CharField(max_length=5,default="none")
    title = models.CharField(max_length=20,default="Assignment title")
    description = models.TextField()
    deadline = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ('deadline',)

    def __str__(self):
        if self.section=='0':
            return f'{self.title}, {self.course}'
        else:
            return f'{self.title}, {self.course} for Section:{self.section}'

    def get_absolute_url(self):
        return reverse('asgn-detail', kwargs={"pk": self.pk})