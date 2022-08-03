from django.contrib.auth.models import AbstractUser
from django.db import models


class Customuser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, unique=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    complete = models.IntegerField(default=1)
    birth_date = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    Number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


class GroupName(models.Model):
    name = models.CharField(null=True, max_length=150, blank=True)

    def __str__(self):
        return self.name


class SubjectName(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class RoomNo(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    DUSHANBA = 'DU'
    SESHANBA = 'SE'
    CHORSHANBA = 'CHO'
    PAYSHANBA = 'PA'
    JUMA = 'JU'
    SHANBA = 'SHA'
    DAYS_OF_THE_WEEK = [
        (DUSHANBA, 'Dushanba'),
        (SESHANBA, 'Seshanba'),
        (CHORSHANBA, 'Chorshanba'),
        (PAYSHANBA, 'Payshanba'),
        (JUMA, 'Juma'),
        (SHANBA, 'Shanba'),
    ]
    group_name = models.ForeignKey(GroupName, on_delete=models.CASCADE)
    week = models.CharField(choices=DAYS_OF_THE_WEEK, max_length=255, default=1)

    def __str__(self):
        return str(self.week) + str('-') + str(self.pk)


class Fanlar(models.Model):
    table = models.ForeignKey(Table, related_name='images', on_delete=models.CASCADE, null=True)
    time = models.TimeField()
    subject_name = models.ForeignKey(SubjectName, on_delete=models.CASCADE, blank=True, null=True)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    room_no = models.ForeignKey(RoomNo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.table.week
