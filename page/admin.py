from django.contrib import admin
# [코드 작성] models.py의 Posting 모델 불러오기
from .models import Posting

# Register your models here.
admin.site.register(Posting)