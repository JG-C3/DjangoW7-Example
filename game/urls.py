from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('rsp/', views.rsp, name="rsp"),
    path('rsp/<str:pick>', views.result, name="result"),
    path('reset/', views.reset, name="reset"),
]
