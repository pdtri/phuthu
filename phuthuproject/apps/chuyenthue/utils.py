
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.template.loader import render_to_string
from django.conf import settings
import weasyprint
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,link_callback=fetch_resources)
    pdf = pisa.pisaDocument(BytesIO(html.encode(encoding='UTF-8',errors='strict')), result)
    #pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + 'css/report.css')])
    ######

    #####
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
"""
def fetch_resources(uri, rel):
    path = os.path.join(settings.STATIC_URL, uri.replace(settings.STATIC_URL, ""))
    return path
"""