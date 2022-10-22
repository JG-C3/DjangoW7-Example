from django.shortcuts import render, redirect
from random import *
# [미션] models.py의 Weapon 모델 불러오기
from .models import Weapon, Character

# Create your views here.
win = 0
draw = 0
lose = 0

def game_list(request):
    return render(request, 'game/game_list.html')

def rsp_select(request):
    global win, draw, lose
    context = {
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_select.html', context)

def rsp_result(request, pick):
    global win, draw, lose
    rsp = ['가위', '바위', '보']
    com = choice(rsp)

    if pick == com:
        result = '무승부'
        draw += 1
    elif (pick == '가위' and com == '보') or (pick == '바위' and com == '가위') or (pick == '보' and com == '바위'):
        result = '승리'
        win += 1
    else :
        result = '패배'
        lose += 1

    context = {
        'pick': pick,
        'com': com,
        'result': result,
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_result.html', context)

def rsp_reset(request):
    global win, draw, lose
    win, draw, lose = 0, 0, 0
    return redirect('game:rsp_select')

def weapon_create(request):
    if request.method == 'POST':
        weapon_name = request.POST.get('weapon-name')
        weapon_power = request.POST.get('weapon-power')
        
        # [미션] Weapon 모델의 name과 content 필드값에 form으로 넘겨준 값을 저장하는 객체 생성
        # [미션] Weapon.objects.create를 사용하여 Weapon 객체 생성
        # [미션] Weapon의 name 필드에 weapon_name 변수 값 저장
        # [미션] Weapon의 power 필드에 weapon_power 변수 값 저장
        Weapon.objects.create(
            name = weapon_name,
            power = weapon_power,
        )
        return redirect('game:weapon_list')
    else:
        return render(request, 'game/weapon_create.html')

def weapon_list(request):
    # [미션] Weapon 모델의 모든 객체를 weapons 리스트로 가져오기
    weapons = Weapon.objects.all()

    context = {
        # [미션] weapons 리스트를 html에 넘겨주기
        # [미션] None을 지우고 작성
        'weapons': weapons,
    }
    return render(request, 'game/weapon_list.html', context)

def character_create(request):
    if request.method == 'POST':
        character_name = request.POST.get('character-name')
        
        Character.objects.create(
            name = character_name,
        )
        return redirect('game:character_list')
    else:
        return render(request, 'game/weapon_create.html')

def character_list(request):
    characters = Character.objects.all()
    if request.method == 'POST':
        character_name = request.POST.get('character-name')
        
        Character.objects.create(
            name = character_name,
        )
        return redirect('game:character_list')

    context = {
        'characters': characters,
    }
    return render(request,'game/character_list.html', context)