from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), # 127.0.0.1:8000
    path('recipes/<int:id>/', views.recipe, name="recipe"), 
]