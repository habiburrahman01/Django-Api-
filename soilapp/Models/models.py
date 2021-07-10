from django.db import models

class soil(models.Model):
    ID = models.IntegerField()
    Name = models.TextField()
    ImagePath = models.ImageField(upload_to="Static/images")
    class Meta:
       managed = False
       db_table = 'soil'
