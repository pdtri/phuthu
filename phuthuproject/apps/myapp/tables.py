# tutorial/tables.py
import django_tables2 as tables
from apps.myapp.models import Congtac
class CongtacTable(tables.Table):
    class Meta:
        model = Congtac
        #add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}