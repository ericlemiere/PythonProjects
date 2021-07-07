from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNum = models.PositiveIntegerField(blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(blank=True, null=False)

    objects = models.Manager

    def __str__(self):
        return self.title, self.courseNum


# english101 = djangoClasses.objects.create(title="ENGLISH", courseNum="101", instructorName="Marge Simpson", duration="5.0")
# english102 = djangoClasses.objects.create(title="ENGLISH", courseNum="102", instructorName="Mr. Burns", duration="5.0")
# physics201 = djangoClasses.objects.create(title="PHYSICS", courseNum="201", instructorName="Pete Livins", duration="5.0")



