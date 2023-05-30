from django.shortcuts import render

class Yarn:
  def __init__(self, name, weight, fiber, description):
    self.name = name
    self.weight = weight
    self.fiber = fiber
    self.description = description

yarns = [
  Yarn('Madelinetosh Tosh Vintage', 'Worsted', '100% Merino Wool', 'Machine wash cold. Air dry flat.'),
  Yarn('Malabrigo Rasta', 'Super Bulky', '100% Merino Wool', 'Hand wash. Dry flat.'),
  Yarn('Malabrigo Silky Merino', 'DK', '51% Silk, 49% Merino Wool', 'Hand wash. Dry flat.'),
  Yarn('Handmaiden Sea Silk', 'Fingering', '70% Silk, 30% Seacell', 'Hand wash.')
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def yarn_index(request):
  return render(request, 'yarns/index.html', { 'yarns': yarns })