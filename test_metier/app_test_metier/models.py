# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json
from datetime import datetime
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class GraphsCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'graphs_category'


class GraphsData(models.Model):
    dt = models.DateTimeField()
    power = models.FloatField()
    json_data = models.TextField()
    installation = models.ForeignKey('GraphsInstallation', models.DO_NOTHING)

    def get_power_and_data(self,cat):
        return [datetime.timestamp(self.dt), json.loads(self.json_data)[cat]]
    @property
    def data(self):
        return json.loads(self.json_data)
    class Meta:
        managed = False
        db_table = 'graphs_data'


class GraphsInstallation(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'graphs_installation'
