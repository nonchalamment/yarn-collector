from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yarn

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
  return render(request, 'yarns/detail.html', { 'yarn': yarn })

class YarnCreate(CreateView):
  model = Yarn
  fields = '__all__'

class YarnUpdate(UpdateView):
  model = Yarn
  fields = ['fiber', 'weight', 'description']

class YarnDelete(DeleteView):
  model = Yarn
  success_url = '/yarns/'