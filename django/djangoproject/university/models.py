import uuid

from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "<id={} name={}>".format(
            self.id, self.name
        )


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return "<name={} capacity={}>".format(
            self.name, self.capacity
        )


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "<name={} room={}>".format(
            self.name, self.room
        )


class Enrolled(models.Model):
    class Meta:
        unique_together = (('student', 'course'),)

    student =models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    credit = models.CharField(max_length=1,blank=True)

    def __str__(self):
        return "<student={} course={} credit={} >".format(
            self.student, self.course, self.credit
        )
