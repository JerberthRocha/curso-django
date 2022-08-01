from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # 127.0.0.1:8000
    path('recipes/<int:id>/', views.recipe), # 127.0.0.1:8000
]