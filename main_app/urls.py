from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('finches/', views.FinchList.as_view(), name='finches_index'), 
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name='finches_detail'), 
]

