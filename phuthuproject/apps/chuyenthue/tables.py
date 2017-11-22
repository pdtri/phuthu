# tutorial/tables.py
import django_tables2 as tables
from apps.chuyenthue.models import TPc
class CongtacTable(tables.Table):
    class Meta:
        model = TPc
        #add class="paleblue" to <table> tag

        attrs = {'class': 'paleblue'}