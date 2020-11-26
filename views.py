import pdfkit
from io import BytesIO

from django.template.loader import get_template
from django.http import HttpResponse

city_name = 'Moscow'
template_src = 'report/test.html'

context = {
    'city': city_name,
    'holidays': [
        {'summary': x.summary, 'date': x.date} for x in
        City.objects.get(name=city_name).order_by('date')
    ]
}

def get_pdf(request):
    template = get_template(template)
    html = template.render(context)
    options = {
        'page-size': 'A4',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response

def listing(request):
    return render(request, template, context)
