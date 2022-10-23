from django.shortcuts import render, redirect
from .models import Posting

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

# Create
def posting_create(request):
    if request.method == 'POST':
        posting_title = request.POST.get('title')
        posting_content = request.POST.get('content')

        Posting.objects.create(
            title=posting_title,
            content=posting_content,
        )
        return redirect('page:posting_list')
    else:
        return render(request, 'page/posting_create.html')

# Read
def posting_list(request):
    postings = Posting.objects.all()
    context = {
        'postings': postings,
    }
    return render(request, 'page/posting_list.html', context)

# Read
def posting_detail(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    context = {
        'posting': posting,
    }
    return render(request, 'page/posting_detail.html', context)

# Update
def posting_update(request, posting_id):
    posting = Posting.objects.get(id=posting_id)

    if request.method == 'POST':
        posting_title = request.POST.get('title')
        posting_content = request.POST.get('content')

        posting.title = posting_title
        posting.content = posting_content
        posting.save()
        return redirect('page:posting_detail', posting_id)
    else:
        context = {
            'posting': posting,
        }
        return render(request, 'page/posting_update.html', context)

# Delete
def posting_delete(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    posting.delete()
    return redirect('page:posting_read')