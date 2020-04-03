from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":

        return HttpResponse('....')


def index(request):
    if request.method == "GET":
        return HttpResponse('...')
    elif request.method == "POST":
        
        
        return HttpResponse('....')
    
    
    
from rbac.models import Permission
def permission_get(request, pk):
    print(pk)
    obj = Permission.objects.all().values('url')
    print(obj[4])
    print(type(obj[4]))
    import json
    # print(json.loads(obj[4].get('url')))
    print(obj[4].get('url'))
    
    ss = {'url': '/host/del/(?P<pk>\d+)/'}
    return HttpResponse(123)