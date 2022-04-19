# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    admin_id = models.IntegerField()
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'admins'


class Category(models.Model):
    cid = models.IntegerField()
    pid = models.IntegerField()
    categories = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Comments(models.Model):
    commid = models.IntegerField()
    pid = models.IntegerField()
    comment = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'comments'


class Experiences(models.Model):
    exid = models.IntegerField()
    uid = models.IntegerField()
    languages = models.CharField(max_length=25, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiences'


class ProjectImages(models.Model):
    piid = models.IntegerField()
    pid = models.IntegerField()
    image = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_images'


class Projects(models.Model):
    pid = models.IntegerField()
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    project_link = models.CharField(max_length=500, blank=True, null=True)
    tutorial_link = models.CharField(max_length=500, blank=True, null=True)
    preview_link = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class Techs(models.Model):
    tid = models.IntegerField()
    pid = models.IntegerField()
    frontend = models.CharField(max_length=90, blank=True, null=True)
    backend = models.CharField(max_length=90, blank=True, null=True)
    languages = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'techs'


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    contact = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=25)
    image = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=9)
    address = models.CharField(max_length=50, blank=True, null=True)
    is_approved = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    approved_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
