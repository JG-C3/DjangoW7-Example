from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting
# [코드 추가] forms.py의 PostingForm 불러오기
from .forms import PostingForm

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

# Create
def posting_create(request):
    if request.method == 'POST':
        # [코드 작성] POST 방식으로 넘어온 값을 form에 저장
        form = PostingForm(request.POST)

        # [코드 작성] form이 유효한지 확인
        if form.is_valid():
            # [코드 작성] posting 객체 생성
            posting = Posting()
            posting.title = form.cleaned_data.get('title')
            posting.content = form.cleaned_data.get('content')

            # [코드 작성] posting 객체 저장
            posting.save()
            return redirect('page:posting_list')
    
    form = PostingForm()
    context = {
        'form': form,
    }
    return render(request, 'page/posting_form.html', context)

# Read
def posting_list(request):
    postings = Posting.objects.all()
    context = {
        'postings': postings,
    }
    return render(request, 'page/posting_list.html', context)

# Read
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    context = {
        'posting': posting,
    }
    return render(request, 'page/posting_detail.html', context)

# Update
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)

    if request.method == 'POST':
        # [코드 작성] POST 방식으로 넘어온 값을 form에 저장
        form = PostingForm(request.POST, instance=posting)

        # [코드 작성] form이 유효한지 확인
        if form.is_valid():
            form.save()
            return redirect('page:posting_detail', posting_id)
    else:
        form = PostingForm(instance=posting)

    context = {
        'form': form,
    }
    return render(request, 'page/posting_form.html', context)

# Delete
def posting_delete(request, posting_id):
    if request.method == 'POST':
        posting = get_object_or_404(Posting, id=posting_id)
        posting.delete()
        return redirect('page:posting_list')
    return redirect('page:posting_detail', posting_id)
