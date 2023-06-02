from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Yarn, Project
from .forms import DustingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def yarn_index(request):
  yarns = Yarn.objects.filter(user = request.user)
  return render(request, 'yarns/index.html', { 'yarns': yarns })

@login_required
def yarn_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  projects_not_made_of_yarn = Project.objects.exclude(id__in = yarn.projects.all().values_list('id'))
  dusting_form = DustingForm()
  return render(request, 'yarns/detail.html', {
    'yarn': yarn,
    'dusting_form': dusting_form,
    'projects': projects_not_made_of_yarn,
    })

@login_required
def add_dusting(request, yarn_id):
  form = DustingForm(request.POST)
  if form.is_valid():
    new_dusting = form.save(commit=False)
    new_dusting.yarn_id = yarn_id
    new_dusting.save()
  return redirect('yarn-detail', yarn_id=yarn_id)

class YarnCreate(LoginRequiredMixin, CreateView):
  model = Yarn
  fields = ['name', 'weight', 'fiber', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class YarnUpdate(LoginRequiredMixin, UpdateView):
  model = Yarn
  fields = ['fiber', 'weight', 'description']

class YarnDelete(LoginRequiredMixin, DeleteView):
  model = Yarn
  success_url = '/yarns/'

class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = '__all__'

class ProjectList(LoginRequiredMixin, ListView):
  model = Project

class ProjectDetail(LoginRequiredMixin, DetailView):
  model = Project

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['name', 'color']

class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects/'

@login_required
def assoc_project(request, yarn_id, project_id):
  Yarn.objects.get(id=yarn_id).projects.add(project_id)
  return redirect('yarn-detail', yarn_id=yarn_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('yarn-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)