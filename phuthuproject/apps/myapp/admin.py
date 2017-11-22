
# Register your models here.
from django.contrib import admin
from apps.myapp.models import Congtac
#from .models import TPc
class Congtacadmin(admin.ModelAdmin):
   list_display = ('id','ten','diachi','congtac')
   search_fields = ('ten', 'congtac')
admin.site.register(Congtac,Congtacadmin)