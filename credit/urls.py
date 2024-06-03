# urls.py
from django.urls import path
from .views import List, Create, Result

app_name = 'credit'

urlpatterns = [
    path('', List.as_view(), name='list'),
    path('credit/', Create.as_view(), name='create'),
    path('result/<int:pk>/', Result.as_view(), name='result'),
]
