# [코드 작성] django의 forms 모듈 불러오기
from django import forms
# [코드 작성] models.py의 Posting, Comment 모델 불러오기
from .models import Posting, Comment

# [코드 작성] forms의 ModelForm을 상속받는 PostingForm 클래스 생성
# [코드 작성] label은 각각 '제목'과 '내용'으로 설정
# [코드 작성] models의 TextField는 forms의 CharField에 widget을 적용하여 구현
# [코드 작성] Meta 클래스를 정의하여 Posting 모델을 기반으로 하고, 어떤 필드를 form으로 사용할 것인지 지정
class PostingForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)

    class Meta:
        model = Posting
        fields = ['title', 'content',]

# [코드 작성] forms의 ModelForm을 상속받는 CommentForm 클래스 생성
# [코드 작성] label은 ''로 설정
# [코드 작성] Meta 클래스를 정의하여 Comment 모델을 기반으로 하고, 어떤 필드를 form으로 사용할 것인지 지정

