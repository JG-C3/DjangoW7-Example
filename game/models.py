from django.db import models

# Create your models here.
# [미션] Weapon 모델을 Class로 생성.
# [미션] models.Model 클래스를 상속받음
# [미션] name : 문자열 필드, 최대 길이 20
# [미션] power : 정수형 필드
class Weapon(models.Model):
    name = models.CharField(max_length=20)
    power = models.IntegerField()

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
