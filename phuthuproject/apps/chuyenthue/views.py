from django.shortcuts import render
from apps.chuyenthue.models import TPc
from .tables import CongtacTable
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

"""
@staff_member_required
def admin_tpc_detail(request, pcid):
	tpc = get_object_or_404(TPc, id=pcid)
	return render(request,'detail.html',{'tpc': tpc})
"""
from django.conf import settings 
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
@staff_member_required
def admin_tpc_pdf(request, pcid):
		tpc = get_object_or_404(TPc, id=pcid)
		html = render_to_string('pdf.html',{'tpc': tpc})
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'filename=\"tpc_{}.pdf"'.format(tpc.id)
		weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
		return response
def chonphieuin(request):
    dk = CongtacTable(TPc.objects.all())
    return render(request, 'thu.html', {'table_ketqua': dk})
class inphieu(View):
    def get(self, request, *args, **kwargs):
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
           return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse ("not fount")