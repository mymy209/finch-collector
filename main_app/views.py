from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

class FinchList(ListView):
    model = Finch

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

