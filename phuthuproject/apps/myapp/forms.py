from django import forms
from apps.myapp.models import Congtac
from django.core.exceptions import ValidationError
#from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.forms import CharField
from django.core import validators
from django import forms
from django.core.validators import validate_email

class CongtacForm(forms.ModelForm):
    class Meta:
        model = Congtac
        fields = ['id','ten', 'diachi', 'congtac']
class SearchForm(forms.Form):
   hovaten = forms.CharField(label='Nhập họ tên tìm kiếm',widget = forms.TextInput(attrs={'size': 32, 'class':'formcontrol'}))