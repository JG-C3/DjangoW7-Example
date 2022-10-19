from django.urls import path
from . import views

app_name = "page"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('read/', views.read, name="read"),
    path('<int:posting_id>/', views.detail, name="detail"),
    path('<int:posting_id>/update/', views.update, name="update"),
    path('<int:posting_id>/delete/', views.delete, name="delete"),
]