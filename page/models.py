from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# [코드 작성] Comment 모델 작성
# [코드 작성] posting, content, date 필드 생성 (posting은 Posting 모델의 객체를 담고 있음)
# [코드 작성] posting 필드는 ForeignKey를 사용하여 Posting 모델의 객체 담고 있음
# [코드 작성] on_delete=models.CASCADE를 사용하면 posting 객체가 삭제될 경우 posting과 연결되어있는 모든 Comment 객체들을 삭제
# [코드 작성] related_name은 posting 객체와 연결되어있는 Comment 객체를 불러오는 경우에 사용
class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comment_list')
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.posting.title} - {self.content[:10]}...'
