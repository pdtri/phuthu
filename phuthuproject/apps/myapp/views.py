from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('<h1>  Phòng Tài nguyên và Môi trường Cái Răng</h1>')