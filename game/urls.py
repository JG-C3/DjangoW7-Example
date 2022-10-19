from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('rsp/', views.rsp, name="rsp"),
    path('rsp/<str:pick>', views.result, name="result"),
    path('reset/', views.reset, name="reset"),
    path('create-weapon/', views.create_weapon, name="create_weapon"),
    path('list-weapon/', views.list_weapon, name="list_weapon"),
]
