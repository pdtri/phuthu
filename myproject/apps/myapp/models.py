from django.db import models
#APP_SCHEMA = "qldd"
# Create your models here.
class Congtac(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=50,blank=True, null=True)
    diachi = models.CharField(max_length=50, blank=True, null=True)
    congtac = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       # db_schema = APP_SCHEMA
        managed = False
        db_table = 'congtac'