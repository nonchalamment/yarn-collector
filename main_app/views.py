from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Yarn, Project
from .forms import DustingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def yarn_index(request):
  yarns = Yarn.objects.all()
  return render(request, 'yarns/index.html', { 'yarns': yarns })

def yarn_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  projects_not_made_of_yarn = Project.objects.exclude(id__in = yarn.projects.all().values_list('id'))
  dusting_form = DustingForm()
  return render(request, 'yarns/detail.html', {
    'yarn': yarn,
    'dusting_form': dusting_form,
    'projects': projects_not_made_of_yarn,
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
  fields = ['name', 'weight', 'fiber', 'description']

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

def assoc_project(request, yarn_id, project_id):
  Yarn.objects.get(id=yarn_id).projects.add(project_id)
  return redirect('yarn-detail', yarn_id=yarn_id)