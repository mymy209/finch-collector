from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    #finch
    path('finches/', views.FinchList.as_view(), name='finches_index'), 
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'), 
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    #feeding
    path('finches/<int:pk>/add_feeding', views.add_feeding, name='add_feeding'),
]

