from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render


#클래스 기반 뷰 (Class base View)

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


# 2. Template base response
class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '완선'
        return context

post_list2 = PostListView2.as_view()


# 3. Json type response
class PostListView3(View):
    #CBV: JSON 형식 응답하기

    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii':False})
    
    def get_data(self):
        return {
            'message' : '안녕, 파이썬 그리고 장고',
            'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS']
            }
post_list3 = PostListView3.as_view()


class ExcelDownloadView(object):
    pass

