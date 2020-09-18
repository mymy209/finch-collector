from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

class FinchList(ListView):
    model = Finch

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'main_app/finch_detail.html', {
    # pass the cat and feeding_form as context
    'finch': finch, 'feeding_form': feeding_form
  })  

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = pk
        new_feeding.save()
    return redirect('finches_detail', finch_id=pk)

