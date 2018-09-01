from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models as geomodels

class Place(models.Model):
    placeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2044)
    src_id = models.CharField(max_length=24, blank=True, null=True)
    dataset = models.CharField(max_length=2044, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'
