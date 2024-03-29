#encoding: utf-8
from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv

def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv'"
    # with open('xx.csv','w') as fp:
    #     csv.writer(fp)
    writer = csv.writer(response)
    writer.writerow(['username','age'])
    writer.writerow(['zhiliao',18])
    return response

def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv'"
    context = {
        'rows': [
            ['username','age'],
            ['zhiliao',18],
        ]
    }
    template = loader.get_template('abc.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response

class Echo:
    def write(self,value):
        return value

def large_csv_view(request):
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='large.csv'"
    rows = ("Row {},{}\n".format(row,row) for row in range(0,1000000))
    response.streaming_content = rows
    return response

    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = "attachment;filename='large.csv'"
    # writer = csv.writer(response)
    # for row in range(0,1000000):
    #     writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    # return response
