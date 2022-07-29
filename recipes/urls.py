from django.urls import path
from .views import home, contato, sobre

urlpatterns = [
    path('', home), # 127.0.0.1:8000
    path('contato/', contato), # 127.0.0.1:8000/contato/
    path('sobre/', sobre), # 127.0.0.1:8000/sobre/
]