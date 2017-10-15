from django.shortcuts import render
#from myproject.apps.myapp.models import MyModel
# Create your views here.
from django.http import HttpResponse
from apps.myapp.models import Congtac
from apps.myapp.forms import CongtacForm
# Create your views here.
def index (request):
    return HttpResponse('<h1>  xin chao ! minh la Ngan chuyen ban la kieng</h1>')
def add_congtac(request):
    saved = False
    if request.method == 'POST':
        form = CongtacForm(request.POST, request.FILES)
        if form.is_valid():
            congtac = Congtac()
            congtac.ten = form.cleaned_data['ten']
            congtac.diachi = form.cleaned_data['diachi']
            congtac.congtac = form.cleaned_data['congtac']
            saved = True
            congtac.save()
    else:
        form = CongtacForm()
    return render(request, 'chuyenthue/nhap/nhap.html', locals())