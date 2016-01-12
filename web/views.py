from django.shortcuts import render
from web.models import *

# Create your views here.
def diagrams(request):
    diagrams = Diagrama.objects.all()
    return render(request,'home.html',{'diagrams':diagrams})

def home(request):
    return render(request, 'index.html', {})
