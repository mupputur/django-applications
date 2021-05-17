from django.db import models

# Create your models here.
# ORM Model to represent a database

#craeted | st_name |  collage


class StudentInfoModel(models.Model):

    st_name = models.CharField(max_length=20)
    collage = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.st_name