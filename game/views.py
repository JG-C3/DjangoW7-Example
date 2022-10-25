from django.shortcuts import render, redirect
from random import *
from .models import Weapon

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
        
        Weapon.objects.create(
            name = weapon_name,
            power = weapon_power,
        )
        return redirect('game:weapon_list')
    else:
        return render(request, 'game/weapon_create.html')

def weapon_list(request):
    weapons = Weapon.objects.all()

    context = {
        'weapons': weapons,
    }
    return render(request, 'game/weapon_list.html', context)

