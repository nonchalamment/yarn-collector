from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Yarn, Project
from .forms import DustingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def yarn_index(request):
  yarns = Yarn.objects.all()
  return render(request, 'yarns/index.html', { 'yarns': yarns })

def yarn_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  dusting_form = DustingForm()
  return render(request, 'yarns/detail.html', {
    'yarn': yarn,
    'dusting_form': dusting_form,
    })

def add_dusting(request, yarn_id):
  form = DustingForm(request.POST)
  if form.is_valid():
    new_dusting = form.save(commit=False)
    new_dusting.yarn_id = yarn_id
    new_dusting.save()
  return redirect('yarn-detail', yarn_id=yarn_id)

class YarnCreate(CreateView):
  model = Yarn
  fields = '__all__'

class YarnUpdate(UpdateView):
  model = Yarn
  fields = ['fiber', 'weight', 'description']

class YarnDelete(DeleteView):
  model = Yarn
  success_url = '/yarns/'

class ProjectCreate(CreateView):
  model = Project
  fields = '__all__'

class ProjectList(ListView):
  model = Project

class ProjectDetail(DetailView):
  model = Project

class ProjectUpdate(UpdateView):
  model = Project
  fields = ['name', 'color']

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects/'