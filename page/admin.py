from django.contrib import admin
# [코드 추가] models.py의 Comment 모델 불러오기
from .models import Posting, Comment

# Register your models here.
admin.site.register(Posting)
# [코드 추가] Comment 모델 등록
admin.site.register(Comment)
