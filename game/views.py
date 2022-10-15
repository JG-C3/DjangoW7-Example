from django.shortcuts import render, redirect
from random import *

# Create your views here.
# win(승리), draw(무승부), lose(패배) 횟수를 저장하는 전역변수 생성
win = 0
draw = 0
lose = 0

def rsp(request):
    # [미션] 함수에서 전역변수 설정하기
    global win, draw, lose

    context = {
        "win": win,
        "draw": draw,
        "lose": lose,
    }
    return render(request, "game/rsp.html", context)

def result(request, pick):
    # [미션] 함수에서 전역변수 설정하기
    global win, draw, lose
    
    rsp = ["가위", "바위", "보"]
    # [미션] 'com' 변수에 'rsp' 리스트의 원소들 중 하나를 랜덤하게 저장하기
    com = choice(rsp)

    # [미션] 내가 선택한 'pick'과 'com' 변수에 저장된 가위바위보 결과를 비교해서 'result' 변수에 결과(승리, 무승부, 패배)를 저장하는 로직 작성하기
    # [미션] win(승리), draw(무승부), lose(패배) 횟수를 가위바위보 결과에 따라 증가시키기
    if pick == com:
        result = "무승부"
        draw += 1
    elif (pick == "가위" and com == "보") or (pick == "바위" and com == "가위") or (pick == "보" and com == "바위"):
        result = "승리"
        win += 1
    else :
        result = "패배"
        lose += 1

    context = {
        "pick": pick,
        # [미션] 'com'키의 value값을 'com'변수값으로 만들기
        "com": com,
        "result": result,
        "win": win,
        "draw": draw,
        "lose": lose,
    }

    return render(request, "game/result.html", context)

def reset(request):
    # [미션] 함수에서 전역변수 설정하기
    global win, draw, lose
    
    # [미션] win(승리), draw(무승부), lose(패배) 횟수를 초기화하기
    win, draw, lose = 0, 0, 0

    # 'urls.py'에서 설정한 app_name인 'games'의 url 경로중 별칭이 'rsp'인 경로로 리다이렉트
    return redirect("game:rsp")