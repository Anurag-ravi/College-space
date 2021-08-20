# Generated by Django 3.2.4 on 2021-08-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[('M.Tech 17', 'M.Tech 17'), ('B.Des 19', 'B.Des 19'), ('B.Tech 19', 'B.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('B.Des 18', 'B.Des 18'), ('M.Tech 16', 'M.Tech 16'), ('B.Des 16', 'B.Des 16'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 17', 'B.Tech 17'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 20', 'M.Tech 20'), ('PhD 18', 'PhD 18'), ('PhD 20', 'PhD 20'), ('B.Tech 16', 'B.Tech 16'), ('B.Tech 18', 'B.Tech 18'), ('B.Des 17', 'B.Des 17'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16'), ('PhD 19', 'PhD 19'), ('B.Des 20', 'B.Des 20')], max_length=13)),
                ('department', models.CharField(choices=[('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemimal Science and Technology', 'Chemimal Science and Technology'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Design', 'Design')], max_length=50)),
                ('section', models.CharField(default='0', max_length=1)),
                ('course', models.CharField(default='none', max_length=5)),
                ('title', models.CharField(default='Assignment title', max_length=20)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'ordering': ('deadline',),
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[('M.Tech 17', 'M.Tech 17'), ('B.Des 19', 'B.Des 19'), ('B.Tech 19', 'B.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('B.Des 18', 'B.Des 18'), ('M.Tech 16', 'M.Tech 16'), ('B.Des 16', 'B.Des 16'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 17', 'B.Tech 17'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 20', 'M.Tech 20'), ('PhD 18', 'PhD 18'), ('PhD 20', 'PhD 20'), ('B.Tech 16', 'B.Tech 16'), ('B.Tech 18', 'B.Tech 18'), ('B.Des 17', 'B.Des 17'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16'), ('PhD 19', 'PhD 19'), ('B.Des 20', 'B.Des 20')], max_length=13)),
                ('department', models.CharField(choices=[('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemimal Science and Technology', 'Chemimal Science and Technology'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Design', 'Design')], max_length=50)),
                ('section', models.CharField(default='0', max_length=1)),
                ('course', models.CharField(default='none', max_length=5)),
                ('title', models.CharField(default='quiz title', max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
