from django.db import models

class Timetable(models.Model):
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

    def __str__(self):
        if self.section=='0':
            return f'{self.batch}, {self.department} Timetable'
        else:
            return f'{self.batch}, {self.department} Section:{self.section} Timetable'



class Monday(models.Model):
    parent = models.OneToOneField(Timetable,on_delete = models.CASCADE)
    eight_nine = models.CharField(max_length = 5) 
    nine_ten = models.CharField(max_length = 5) 
    ten_eleven = models.CharField(max_length = 5) 
    eleven_twelve = models.CharField(max_length = 5) 
    twelve_one = models.CharField(max_length = 5) 
    two_three = models.CharField(max_length = 5)
    three_four = models.CharField(max_length = 5)
    four_five = models.CharField(max_length = 5)
    five_six = models.CharField(max_length = 5)

    def __str__(self):
        if self.parent.section=='0':
            return f'Monday {self.parent.batch}, {self.parent.department} Timetable'
        else:
            return f'Monday {self.parent.batch}, {self.parent.department} Section:{self.parent.section} Timetable'
        

class Tuesday(models.Model):
    parent = models.OneToOneField(Timetable,on_delete = models.CASCADE)
    eight_nine = models.CharField(max_length = 5)
    nine_ten = models.CharField(max_length = 5)
    ten_eleven = models.CharField(max_length = 5)
    eleven_twelve = models.CharField(max_length = 5)
    twelve_one = models.CharField(max_length = 5)
    two_three = models.CharField(max_length = 5)
    three_four = models.CharField(max_length = 5)
    four_five = models.CharField(max_length = 5)
    five_six = models.CharField(max_length = 5)

    def __str__(self):
        if self.parent.section=='0':
            return f'Tuesday {self.parent.batch}, {self.parent.department} Timetable'
        else:
            return f'Tuesday {self.parent.batch}, {self.parent.department} Section:{self.parent.section} Timetable'

class Wednesday(models.Model):
    parent = models.OneToOneField(Timetable,on_delete = models.CASCADE)
    eight_nine = models.CharField(max_length = 5)
    nine_ten = models.CharField(max_length = 5)
    ten_eleven = models.CharField(max_length = 5)
    eleven_twelve = models.CharField(max_length = 5)
    twelve_one = models.CharField(max_length = 5)
    two_three = models.CharField(max_length = 5)
    three_four = models.CharField(max_length = 5)
    four_five = models.CharField(max_length = 5)
    five_six = models.CharField(max_length = 5)

    def __str__(self):
        if self.parent.section=='0':
            return f'Wednesday {self.parent.batch}, {self.parent.department} Timetable'
        else:
            return f'Wednesday {self.parent.batch}, {self.parent.department} Section:{self.parent.section} Timetable'
class Thursday(models.Model):
    parent = models.OneToOneField(Timetable,on_delete = models.CASCADE)
    eight_nine = models.CharField(max_length = 5)
    nine_ten = models.CharField(max_length = 5)
    ten_eleven = models.CharField(max_length = 5)
    eleven_twelve = models.CharField(max_length = 5)
    twelve_one = models.CharField(max_length = 5)
    two_three = models.CharField(max_length = 5)
    three_four = models.CharField(max_length = 5)
    four_five = models.CharField(max_length = 5)
    five_six = models.CharField(max_length = 5)

    def __str__(self):
        if self.parent.section=='0':
            return f'Thursday {self.parent.batch}, {self.parent.department} Timetable'
        else:
            return f'Thursday {self.parent.batch}, {self.parent.department} Section:{self.parent.section} Timetable'

class Friday(models.Model):
    parent = models.OneToOneField(Timetable,on_delete = models.CASCADE)
    eight_nine = models.CharField(max_length = 5)
    nine_ten = models.CharField(max_length = 5)
    ten_eleven = models.CharField(max_length = 5)
    eleven_twelve = models.CharField(max_length = 5)
    twelve_one = models.CharField(max_length = 5)
    two_three = models.CharField(max_length = 5)
    three_four = models.CharField(max_length = 5)
    four_five = models.CharField(max_length = 5)
    five_six = models.CharField(max_length = 5)

    def __str__(self):
        if self.parent.section == '0':
            return f'Friday {self.parent.batch}, {self.parent.department} Timetable'
        else:
            return f'Friday {self.parent.batch}, {self.parent.department} Section:{self.parent.section} Timetable'

