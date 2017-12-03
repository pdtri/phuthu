from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class TPc(models.Model):
    #pcid = models.AutoField(primary_key= True)
    pcid = models.AutoField(primary_key=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    soin = models.CharField(max_length=50, blank=True, null=True)
    ngaychuyen = models.DateTimeField(blank=True, null=True)
    hovaten = models.CharField(max_length=250, blank=True, null=True)
    diachi = models.CharField(max_length=250, blank=True, null=True)
    thuadatso = models.CharField(max_length=250, blank=True, null=True)
    tobando = models.CharField(max_length=250, blank=True, null=True)
    dcthuadat = models.CharField(max_length=250, blank=True, null=True)
    loaiduong = models.CharField(max_length=250, blank=True, null=True)
    hangdat = models.CharField(max_length=50, blank=True, null=True)
    vitri = models.CharField(max_length=255, blank=True, null=True)
    loaidat = models.CharField(max_length=250, blank=True, null=True)
    mdsudung = models.CharField(max_length=250, blank=True, null=True)
    thsudung = models.CharField(max_length=50, blank=True, null=True)
    odlaudai = models.CharField(max_length=50, blank=True, null=True)
    cthtungay = models.CharField(max_length=50, blank=True, null=True)
    cthdenngay = models.CharField(max_length=50, blank=True, null=True)
    dientich = models.CharField(max_length=250, blank=True, null=True)
    dtnt = models.CharField(max_length=250, blank=True, null=True)
    dtnttronghm = models.CharField(max_length=250, blank=True, null=True)
    dtnttrenhm = models.CharField(max_length=250, blank=True, null=True)
    dtdt = models.CharField(max_length=250, blank=True, null=True)
    dtdtsdr = models.CharField(max_length=250, blank=True, null=True)
    dtdtsdc = models.CharField(max_length=250, blank=True, null=True)
    nguongoc = models.CharField(max_length=250, blank=True, null=True)
    thoidiemsdd = models.CharField(max_length=250, blank=True, null=True)
    noptien100 = models.NullBooleanField()
    noptien50 = models.NullBooleanField()
    noptien50clld = models.NullBooleanField()
    noptienclld = models.NullBooleanField()
    capnha = models.CharField(max_length=255, blank=True, null=True)
    dtsannha = models.CharField(max_length=250, blank=True, null=True)
    sotangnha = models.CharField(max_length=255, blank=True, null=True)
    nguongocnha = models.CharField(max_length=255, blank=True, null=True)
    ngayhoancong = models.CharField(max_length=50, blank=True, null=True)
    doituongkpn = models.CharField(max_length=255, blank=True, null=True)
    doitongbtth = models.CharField(max_length=255, blank=True, null=True)
    nhanvien = models.CharField(max_length=100, blank=True, null=True)
    loaihoso = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.hovaten
    def __str__(self):
        return self.hovaten
    class Meta:
        managed = False
        db_table = 't_pc'

