# dojo/views.py
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Function Base View! 함수기반 VIEW! 의 4가지 패턴 (2-6)
#1. number sum in path
def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

#2. direct response!
def hello(request, name, age):
    return HttpResponse(f'안녕하세요. {name}님, {age}살 이시군요.') 

#3. Http response!
def post_list1(request):
    name = '완선'
    return HttpResponse('''
<h1>post_list1 결과페이지</h1>
<p>{name}</p>
<p>결과 페이지 끝 입니다.</p>'''.format(name=name))

#4. template rendering!
def post_list2(request):
    name = '완선'
    return render(request, 'dojo/post_list2.html', {'name_':name})

#5. json type response!
def post_list3(request):
    return JsonResponse({
        'message':'안녕 파이썬&장고',
        'items':['파이썬','장고','Celery','Azure','AWS'],
        }, json_dumps_params={'ensure_ascii': False})

#6. xls_file download!
def excel_download(request):
   # filepath = '/home/sean/dev/myproject/201502051448266225.xls' 
    filepath = os.path.join(settings.BASE_DIR, '201502051448266225.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # default => 'text/html
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

#def mysum(request, x=0, y=0, z=0):
    #request : HttpRequest
#    return HttpResponse(int(x) + int(y) + int(z))

# Create your views here.
