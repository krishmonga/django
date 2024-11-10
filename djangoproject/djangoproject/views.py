from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, Django! learning new things is fun')
    return render(request, 'index.html')
def about(request):
    return HttpResponse('Hello, Django! about page')

def contact(request):
    return HttpResponse('Hello, Django! contacting new persons is fun')