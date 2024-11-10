from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'djangoapp/django.html')  # Corrected path for the template
