# Generated by Django 3.2.4 on 2021-08-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210820_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='batch',
            field=models.CharField(choices=[('PhD 16', 'PhD 16'), ('B.Des 16', 'B.Des 16'), ('M.Tech 18', 'M.Tech 18'), ('B.Des 17', 'B.Des 17'), ('PhD 17', 'PhD 17'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 19', 'M.Tech 19'), ('B.Des 20', 'B.Des 20'), ('PhD 19', 'PhD 19'), ('B.Tech 16', 'B.Tech 16'), ('PhD 18', 'PhD 18'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 16', 'M.Tech 16'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 20', 'B.Tech 20'), ('PhD 20', 'PhD 20'), ('B.Des 19', 'B.Des 19'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 19', 'B.Tech 19'), ('B.Des 18', 'B.Des 18')], max_length=13),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='department',
            field=models.CharField(choices=[('Design', 'Design'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemimal Science and Technology', 'Chemimal Science and Technology'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='batch',
            field=models.CharField(choices=[('PhD 16', 'PhD 16'), ('B.Des 16', 'B.Des 16'), ('M.Tech 18', 'M.Tech 18'), ('B.Des 17', 'B.Des 17'), ('PhD 17', 'PhD 17'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 19', 'M.Tech 19'), ('B.Des 20', 'B.Des 20'), ('PhD 19', 'PhD 19'), ('B.Tech 16', 'B.Tech 16'), ('PhD 18', 'PhD 18'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 16', 'M.Tech 16'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 20', 'B.Tech 20'), ('PhD 20', 'PhD 20'), ('B.Des 19', 'B.Des 19'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 19', 'B.Tech 19'), ('B.Des 18', 'B.Des 18')], max_length=13),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='department',
            field=models.CharField(choices=[('Design', 'Design'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemimal Science and Technology', 'Chemimal Science and Technology'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering')], max_length=50),
        ),
    ]