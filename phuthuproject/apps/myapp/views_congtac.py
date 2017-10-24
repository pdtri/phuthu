
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404

from apps.myapp.models import Congtac
from apps.myapp.forms import CongtacForm
#from chuyenthue.models import f_tpc_nhap
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from apps.myapp.forms import SearchForm

#from cart.forms import CartAddProductForm
#from .recommender import Recommender
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from django.shortcuts import render_to_response
from django.template import Context
from .tables import CongtacTable
from django_tables2 import RequestConfig
#
import json

def add_congtac(request):
    saved = False
    if request.method == 'POST':
            form = CongtacForm(request.POST, request.FILES)
            if form.is_valid():
                congtac = Congtac()
                congtac.ten = form.cleaned_data['ten']
                congtac.diachi = form.cleaned_data['diachi']
                congtac.congtac = form.cleaned_data['congtac']
#                congtac.id = form.cleaned_data['id']
                saved = True
                congtac.save()
    else:
             form = CongtacForm()

    return render(request, 'nhap_congtac.html', locals())
class tim_congtac(View):
    """Search all tweets with query /search/?query=<query> URL"""
    def get(self, request):
        #try:
            #selected_item = TPc.objects.all()
            #form = f_tpc_nhap(data=selected_item)
            #form = SearchForm()
            #form = data['hovaten']
            #form = TPc.objects.filter("hovaten")
            #TPc.__dict__['hovaten']['diachi']
            #form = TPc.fields['hovaten']
			#myForm.fields['description']
        #except Congtac.DoesNotExist:
        #    raise Http404("get bi loi")
       #
        #form = f_tpc_nhap()
        #params = dict()
        #params={}
        #params['query'] = None
        #params["form"] = form
        #return render(request, 'tim_congtac.html', params)
        #dk = CongtacTable(Congtac.objects.filter(ten__icontains= "null"))
        dk = CongtacTable(Congtac.objects.all())
        return render(request, 'tim_congtac.html', {'table_ketqua': dk})
    def post(self, request):
        if request.method == 'POST':
                #form = f_tpc_nhap(request.POST)
                     #if form.is_valid():
            #form = f_tpc_nhap(request.POST)# or None)
                    form = SearchForm(request.POST)# or None)
            #form = data['hovaten']
                     #form = AuthenticationForm(request.POST)
            #if  form.is_valid():
                 #try:
                       
                    #hovaten = form.cleaned_data['hovaten']
                    dk_ten = request.POST.get('ten')
                     #dk = TPc.objects.filter(hovaten__icontains = hovaten)
                     #context = Context({"TPc": hovaten, "dk": dk })
                     #return render(request, 'chuyenthue/nhap/_tweet_search.html',   context)
                    dk = CongtacTable(Congtac.objects.filter(ten__icontains = dk_ten))
                    #dk = CongtacTable(Congtac.objects.all())
                    #table=PersonTable(dk)
                    RequestConfig(request).configure(dk)
                    return render(request, 'tim_congtac.html', {'table_ketqua': dk})
					 
                     #return HttpResponse( 'chuyenthue/nhap/_tweet_search.html', context)
                     #return HttpResponse(json.dumps(return_str),content_type="application/json")
                # except:
                 #    print("loi roi nhung form).is_valid = true")
            #else:
            #     loi={}
            #     loi= print(form.is_valid(), form.errors, type(form.errors))
            #     return HttpResponse(loi)
                 #HttpResponseRedirect("/search")
        else:
                #dk = CongtacTable(Congtac.objects.all())
                HttpResponseRedirect("tim_congtac.html" )


class thu(View):
    """Search all tweets with query /search/?query=<query> URL"""

    def get(self, request):

        dk = CongtacTable(Congtac.objects.all())
        return render(request, 'thu.html', {'table_ketqua': dk})

    def post(self, request):
        if request.method == 'POST':

            form = SearchForm(request.POST)  # or None)

            dk_ten = request.POST.get('ten')

            dk = CongtacTable(Congtac.objects.filter(ten__icontains=dk_ten))
            # dk = CongtacTable(Congtac.objects.all())
            # table=PersonTable(dk)
            RequestConfig(request).configure(dk)
            return render(request, 'thu.html', {'table_ketqua': dk})
        else:
            HttpResponseRedirect("thu.html")