# Generated by Django 3.2.4 on 2021-08-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210820_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='batch',
            field=models.CharField(choices=[('M.Tech 16', 'M.Tech 16'), ('B.Tech 18', 'B.Tech 18'), ('M.Tech 19', 'M.Tech 19'), ('PhD 17', 'PhD 17'), ('PhD 20', 'PhD 20'), ('M.Tech 20', 'M.Tech 20'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 20', 'B.Tech 20'), ('B.Des 17', 'B.Des 17'), ('B.Tech 16', 'B.Tech 16'), ('M.Tech 17', 'M.Tech 17'), ('B.Des 18', 'B.Des 18'), ('B.Des 19', 'B.Des 19'), ('PhD 19', 'PhD 19'), ('PhD 16', 'PhD 16'), ('B.Des 20', 'B.Des 20'), ('PhD 18', 'PhD 18'), ('B.Des 16', 'B.Des 16'), ('M.Tech 18', 'M.Tech 18'), ('B.Tech 19', 'B.Tech 19')], max_length=13),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='department',
            field=models.CharField(choices=[('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Civil Engineering', 'Civil Engineering'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Design', 'Design'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemimal Science and Technology', 'Chemimal Science and Technology'), ('Engineering Physics', 'Engineering Physics'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering')], max_length=50),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='remove_after',
            field=models.CharField(choices=[('After 1 week', 'After 1 week'), ('After 1 month', 'After 1 month'), ('After 1 day', 'After 1 day'), ('After 3 day', 'After 3 day'), ('After This Semester', 'After This Semester'), ('After 2 week', 'After 2 week')], max_length=20),
        ),
    ]
