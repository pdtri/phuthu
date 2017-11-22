
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
#from .rendering import render_to_pdf
from django.shortcuts import render
from django.shortcuts import render_to_response
from apps.chuyenthue.forms import SelectFileForm
import csv
import datetime
from django.template.loader import render_to_string
from django.conf import settings
import weasyprint
from django.conf.urls.static import static
import json
import os
#from django.http import HttpResponse

# Register your models here.

from apps.chuyenthue.models import TPc

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    #selected = request.POST.getlist('checks[]')
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

def capnhat(modeladmin,request,queryset):
	queryset.update(loaihoso='CN')
def khongcapnhat(modeladmin,request,queryset):
	queryset.update(loaihoso='TK')

def select_file_action(modeladmin, request, queryset):
    form = None
    if 'apply' in request.POST:
        form = ChooseFileForm(request.POST)
        if form.is_valid():
            file = form.cleaned_data['file']
            count = 0
            for item in queryset:
                # do something with file
                item.file = file
                item.save()
                count += 1
            modeladmin.message_user(request, "File successfully selected")
            return HttpResponseRedirect(request.get_full_path())

    if not form:
        form = SelectFileForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

    return render(request, 'select_file.html', {'items': queryset, 'form': form, 'title': 'File'})

select_file_action.short_description = "Choose file"


"""
class inphieuchuyen(View):
    def get(self, request, *args, **kwargs):
    #def inphieuchuyen(modeladmin, request, queryset):
        template = get_template('inphieu.html')
        context = {
              'today': '04/11/2017',
              'amount': 39.99,
             'customer_name': 'Cooper Mann',
             'order_id': 1233434,
        }
        html = template.render(context)
        pdf = render_to_pdf('inphieu.html', context )
        if pdf:
           #return HttpResponse (pdf, content_type='application/pdf')
           return render( request,pdf, content_type='application/pdf')
        return HttpResponse ("not fount")
"""


def inphieuchuyen(self, modeladmin, request, *args, **kwargs):
    # def inphieuchuyen(modeladmin, request, queryset):
    context = ['get_status_display()']
    #context = get_status_display()
    # template = get_template('inphieu.html')
    """
    context = {
        'today': '04/11/2017',
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
    }
    """
    # html = template.render(context)
    pdf = render_to_pdf('inphieu.html', context)
    # if pdf:
    return HttpResponse(pdf, content_type='application/pdf')

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \ filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
               value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

def to_pdf(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        # template = get_template('inphieu.html')
        # if pdf:
        #return HttpResponse(pdf, content_type='application/pdf')
	    #response = HttpResponse(pdf,content_type='application/pdf')
	    #response['Content-Disposition'] = 'attachment; \ filename={}.csv'.format(opts.verbose_name)
	    #writer = csv.writer(response)
        fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
        # Write a first row with header information
	    #writer.writerow([field.verbose_name for field in fields])
	    # Write data rows

        data_row = []
        for obj in queryset:
            dict_row = {}
            for  field in fields:
                value =  getattr(obj, field.name)
                dict_row[field.verbose_name]=value
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                    dict_row[field.verbose_name] =  value
            data_row.append(dict(dict_row))


        """
        context = {
        'today': '04/11/2017',
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
        }
        """

        #@staff_member_required
        #def admin_order_pdf(request, order_id):
            #order = get_object_or_404(Order, id=order_id)
            #html = render_to_string('orders/order/pdf.html', {'order': order})

        html = render_to_string('inphieu.html', {"data_row": data_row})
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order.id)
        #response['Content-Disposition'] = 'filename=\"thu.pdf"'.format(1)
        #chuoi= 'D:\hoclamweb\myfolderproject\phuthuproject\static\css\inphieu.css'
        BASE_DIR = os.path.dirname((__file__))
        chuoi = str(BASE_DIR)+'/static/css/inphieu.css'
        weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(chuoi)])
        return response
        #contex = json.dumps(data_row)
        #html = template.render(contex)
        #pdf = render_to_pdf('inphieu.html', context)
        #pdf = render_to_pdf('inphieu.html', {"data_row": data_row})
        #pdf = html_to_pdf('inphieu.html', {"data_row": data_row})
        #return HttpResponse(pdf, content_type='application/pdf')
        #return HttpResponse(pdf, content_type='application/pdf')
        #return render(request,'inphieu.html', {"data_row": data_row}) chay duoc
        #return render_to_response('inphieu.html',{"data_row": data_row})
export_to_csv.short_description = 'Export to pdf'
#from django.core.urlresolvers import reverse
#def tpc_detail(obj):
#	return '<a href="{}">View</a>'.format(reverse('orders:admin_tpc_detail', args=[obj.id]))
#tpc_detail.allow_tags = True 
def tpc_pdf(obj):
	return '<a href="{}">PDF</a>'.format(reverse('orders:admin_tpc_pdf', args=[obj.id]))
tpc_pdf.allow_tags = True
tpc_pdf.short_description = 'PDF bill'
class TPcAdmin (admin.ModelAdmin):
    list_display = (
        #'tpc_detail',
        'pcid',
        'so',
        'so_in',
        'ngaychuyen',
        'hovaten',
        'diachi',
        'thuadatso',
        'tobando',
        'dc_thuadat',
        'loaiduong',
        'hangdat',
        'vitri',
        'loaidat',
        'md_sudung',
        'th_sudung',
        'od_laudai',
        'cth_tungay',
        'cth_denngay',
        'dientich',
        'dtnt',
        'dtnt_trong_hm',
        'dtnt_tren_hm',
        'dtdt',
        'dtdt_sdr',
        'dtdt_sdc',
        'nguongoc',
        'thoidiem_sdd',
        'noptien_100',
        'noptien_50',
        'noptien_50_clld',
        'noptien_clld',
        'capnha',
        'dt_sannha',
        'sotangnha',
        'nguongocnha',
        'ngay_hoancong',
        'doituong_kpn',
        'doitong_btth',
        'nhanvien',
        'loaihoso',
        
    )

    """
     for seat in Seat.objects.all():
        for xx in y[seat.row]:
            if xx == seat.column:
                y[seat.row].update({seat.column: seat})
    
    return render_to_response('seatmap/seatmap.html', {'grid':y})
    def inphieuchuyen(self, modeladmin, request,  *args, **kwargs):
        # def inphieuchuyen(modeladmin, request, queryset):
        context = ['get_status_display']
        #template = get_template('inphieu.html')
        
        context = {
            'today': '04/11/2017',
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        
        #html = template.render(context)
        pdf = render_to_pdf('inphieu.html', context)
        # if pdf:
        return HttpResponse (pdf, content_type='application/pdf')
        # return render( request,pdf, content_type='application/pdf')
        #return render(request, pdf)
        # return HttpResponse ("not fount")
   
    def get_status(self, obj):
        return obj.get_status_display()

    get_status.short_description = 'inphieu'
    """
    list_filter = ( 'ngaychuyen', 'hovaten','dc_thuadat')
    search_fields = ('ngaychuyen', 'hovaten')
    list_display_links=['ngaychuyen']
    list_editable=['hovaten']
    #prepopulated_fields = {'hovaten': ('ngaychuyen',)}
    #raw_id_fields = ('hovaten',)
    exclude = ('created_at', 'updated_at')
    date_hierarchy = 'ngaychuyen'
    ordering = ['hovaten', 'ngaychuyen']

    def hovaten(self, obj):
        return obj.get_status_display()
        hovaten.admin_order_field = 'hovaten'
        hovaten.short_description = 'hovaten'
    actions = [capnhat,khongcapnhat,select_file_action,hovaten,export_to_csv,to_pdf]
admin.site.register(TPc,TPcAdmin)
#admin.site.register(M, MAdmin,obj)
admin.site.add_action(export_selected_objects, 'export_selected')
