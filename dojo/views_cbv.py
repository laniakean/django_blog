#views_cbv.py 정의
#기능 : 클래스 기반 뷰 (Class Base View) // views.py에는 함수 기반 뷰 제공
#각각에 클래스에 따라 다른 형태나 방식으로 뷰 제공

#---------------Importing Section-------------------
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render
import datetime
import os
#---------------------------------------------------

#========== First CBV : 인자값을 활용한 html을 바로 반환=============
#1. direct response!
class PostListView1(View):
    def get(self, request):
        name = 'sean'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
                <h1>This is Heading</h1>
                <p>Hi, {name}!</p>
                <p>It is pleasure to meet you!</p>
                '''
post_list1 = PostListView1.as_view()
#================================================================


#==== Second CBV : Template 을 활용 한 Html 반환 =====
# 2. Template base response
class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '완선'
        return context
post_list2 = PostListView2.as_view()
#=====================================================


#=======================Third CBV : Json type data를 반환하기 ==========================
# 3. Json type response
class PostListView3(View):
    #CBV: JSON 형식 응답하기

    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii':False})
    
    def get_data(self):
        date = datetime.datetime.now()
        return {
            'message' : '안녕, 파이썬 그리고 장고',
            'message_type' : 'Json_api',
            'items' : [
                    '파이썬', 
                    '장고', 
                    'Celery', 
                    'Azure', 
                    'AWS'
            ],
            'requested_at' : date ,
            }
post_list3 = PostListView3.as_view()
#===========================================================================================

# 4. Excel Download



#=======================Forth CBV : Excel Download / 파일  반환하기 ==========================
class ExcelDownloadView(View):
    excel_path = '/home/sean/dev/myproject/201502051448266225.xls'

    def get(self, request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
            response['Content-Disposition']='attachment; filename="{}"'.format(filename)
            return response
excel_download = ExcelDownloadView.as_view()

