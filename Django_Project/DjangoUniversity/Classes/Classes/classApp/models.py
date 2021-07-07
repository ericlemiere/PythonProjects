from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNum = models.IntegerField(blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} {}".format(self.title.upper(), str(self.courseNum))
        # this returns a formatted string of "Title CourseNum"
        # example: "ENGLISH 101"
