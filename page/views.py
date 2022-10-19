from django.shortcuts import render, redirect
# [미션] models.py의 Posting 모델 불러오기
from .models import Posting

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def create(request):
    # 만약 form에서 값을 전송하는 방식이 'POST'일 경우
    if request.method == 'POST':
        # POST 방식으로 넘어온 값 중 'title'과 'content'의 값을 딕셔너리 형태로 반환
        posting_title = request.POST.get('title')
        posting_content = request.POST.get('content')

        # [미션] Posting 모델의 title과 content 필드값에 form으로 넘겨준 값을 저장하는 객체 생성
        Posting.objects.create(
            title=posting_title,
            content=posting_content,
        )
        # 앱 이름이 'page'인 urls.py에서 name 속성값이 'read'인 url로 리다이렉트
        return redirect('page:read')
    else:
        return render(request, 'page/create.html')

def read(request):
    # [미션] Posting 모델의 모든 객체를 리스트로 가져오기
    postings = Posting.objects.all()
    context = {
        # [미션] context를 이용하여 postings 리스트를 딕셔너리 형식으로 html에 넘겨주기
        # [미션] None을 지우고 작성
        'postings': postings,
    }
    return render(request, 'page/read.html', context)

def detail(request, posting_id):
    # [코드 작성] Posting 모델의 객체 중 id 값이 posting_id와 같은 객체를 가져옴
    posting = Posting.objects.get(id=posting_id)
    context = {
        # [코드 수정] posting 객체에 저장되어있는 값을 html에 넘겨주기
        # [코드 수정] None을 지우고 작성
        'posting': posting,
    }
    return render(request, 'page/detail.html', context)

def update(request, posting_id):
    # [코드 작성] Posting 모델의 객체 중 id 값이 posting_id와 같은 객체를 가져옴
    posting = Posting.objects.get(id=posting_id)

    # 만약 form에서 값을 전송하는 방식이 'POST'일 경우
    if request.method == 'POST':
        # [코드 작성] POST 방식으로 넘어온 값 중 'title'과 'content'의 값을 딕셔너리 형태로 반환
        posting_title = request.POST.get('title')
        posting_content = request.POST.get('content')

        # [코드 작성] posting 객체의 title과 content 필드값에 form으로 넘겨준 값을 각각 넣어줌
        posting.title = posting_title
        posting.content = posting_content

        # [코드 작성] posting 객체의 변경사항 저장
        posting.save()
        # 앱 이름이 'page'인 urls.py에서 name 속성값이 'detail'인 url로 리다이렉트
        return redirect('page:detail', posting_id)
    else:
        context = {
            # [코드 수정] posting 객체에 저장되어있는 값을 html에 넘겨주기
            # [코드 수정] None을 지우고 작성
            'posting': posting,
        }
        return render(request, 'page/update.html', context)

def delete(request, posting_id):
    # [코드 작성] Posting 모델의 객체 중 id 값이 posting_id와 같은 객체를 가져옴
    posting = Posting.objects.get(id=posting_id)
    # [코드 작성] posting 객체 삭제
    posting.delete()
    return redirect('page:read')