from django.shortcuts import render
from web.models import *
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponse
from suds.xsd.doctor import ImportDoctor, Import
from suds.client import Client
# Create your views here.

def login(request):
    if request.method == 'POST':
        try:
            user = request.POST['user'].strip()
            pwd = request.POST['pwd'].strip()
        except:
            return HttpResponseBadRequest('Error parametros')
        from django.contrib.auth import authenticate, login
        auth = authenticate(username = user , password = pwd)
        if auth is not None:
            login(request, auth)
            return HttpResponse()
        else:
            url = 'http://ws.espol.edu.ec/saac/wsandroid.asmx?WSDL'
            imp = Import('http://www.w3.org/2001/XMLSchema')
            imp.filter.add('http://tempuri.org/')
            doctor = ImportDoctor(imp)
            client = Client(url, doctor=doctor)
            auth = client.service.autenticacion(user,pwd)
            if auth == True:
                auth = User.objects.create_user(username=user, password=pwd)
                auth.save()
                auth = authenticate(username = user , password = pwd)
                login(request, auth)
                return HttpResponse()
            else:
                return HttpResponseForbidden('Autenticacion Fallida')
    else:
        return HttpResponseBadRequest()

# Create your views here.
def diagrams(request):
    diagrams = Diagramas.objects.all()
    return render(request,'home.html',{'diagrams':diagrams})

def home(request):
    return render(request, 'index.html', {})
