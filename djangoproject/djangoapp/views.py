from django.shortcuts import render
from.models import ChaiVarity
# Create your views here.

def index(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'djangoapp/django.html',{'chais':chais})  # Corrected path for the template


def chai(request):
    return render(request, 'djangoapp/all_chai.html')  # Corrected path for the template

from .models import      Store
from .forms import ChaiVarietyForm

def chai_store_view(request):
  stores = None
  if request.method == 'POST':
    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)
  else:
    form = ChaiVarietyForm()

  return render(request, 'chai/chai_stores.html', {'form': form, 'stores': stores})