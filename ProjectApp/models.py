from django.db import models



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

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'users'


# Create your models here.
class Projects(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    project_link = models.CharField(max_length=500, blank=True, null=True)        
    tutorial_link = models.CharField(max_length=500, blank=True, null=True)       
    preview_link = models.CharField(max_length=250, blank=True, null=True)        

    class Meta:
        managed = False
        db_table = 'projects'