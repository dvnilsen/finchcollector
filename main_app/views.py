from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Tree 
from .forms import FeedingForm

#finches = [
#  {'name': 'Lolo', 'color': 'Yellow', 'gender': 'female', 'location': 'North America'},
#  {'name': 'Sachi', 'color': 'White', 'gender': 'male', 'location': 'Europe'},
#]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.trees.all().values_list('id')
  trees_finch_doesnt_have = Tree.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, "finches/detail.html", {
    "finch": finch, "feeding_form": feeding_form,
    'trees': trees_finch_doesnt_have
  })

class FinchCreate(CreateView):
  model = Finch
  fields = ["name", "color", "gender", "location"]

class FinchUpdate(UpdateView):
  model = Finch
  fields = "__all__"

class FinchDelete(DeleteView):
  model = Finch
  success_url = "/finches"

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class TreeList(ListView):
  model = Tree

class TreeDetail(DetailView):
  model = Tree

class TreeCreate(CreateView):
  model = Tree
  fields = '__all__'

class TreeUpdate(UpdateView):
  model = Tree
  fields = '__all__'

class TreeDelete(DeleteView):
  model = Tree
  success_url = '/trees'

def assoc_tree(request, finch_id, tree_id):
  Finch.objects.get(id=finch_id).trees.add(tree_id)
  return redirect('detail', finch_id=finch_id)