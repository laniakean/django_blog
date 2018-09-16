# blog/models.py
# 모델의 역할은 DB에서 데이터를 가져오는 역할
# 모든 클래스는 단수형으로 쓴다!
import re
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid lnglat Type')




class Post(models.Model):
    title = models.CharField(max_length = 100, 
            verbose_name = '제목',
            help_text = '포스트 제목을 입력해 주세요. 최대 100자',
            #choices = (
               # ('news','[뉴스]'), #('저장될 값', 'UI에 보여질 레이블')  
               # ('tech','[기술]'),
               # ('comp','[컴퓨터]'),
               # ('litreature','[인문]'),
               # )
            ) #글자의 길이 제한이 있는 문자열! (길이제한 : CharField 사용)
    content = models.TextField(verbose_name = '내용')               #글자의 길이 제한이 없는 문자열! (길이무제한 : TextField 사용)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add : 최초 생성일을 입력하는 방식(일시)
    updated_at = models.DateTimeField(auto_now=True)     #auto_now : 파일이 새로 저장된 일자를 입력하는 방식(일시)

    tags = models.CharField(max_length = 100, blank=True)
    lnglat = models.CharField(max_length = 50,
        validators = [lnglat_validator],
        help_text = "경도와 위도 포멧으로 입력해 주세요.",
        blank = True    
    )




# Create your models here.

