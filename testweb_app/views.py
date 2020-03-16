from django.shortcuts import render
from django import http
from django.shortcuts import render
from django import http
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from testweb_app.forms import StressForm
import os, time


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testweb_app.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#def index(request):
#    http_host = request.META['HTTP_HOST']
#    host = {'http_host': http_host}
#    return render(request, 'index.html', host)
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'login.html')#,  context=RequestContext(request))
    #return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def main(request):
    http_host = request.META['HTTP_HOST']
    host = {'http_host': http_host}
    return render(request, 'index.html', host)

def stress_test(request):
    '''
        Does CPU stress, select the number of CPU's and the time for stress
    '''
    if request.method == 'POST':
        form = StressForm(request.POST)
        if form.is_valid():
            cpu = form.cleaned_data['CPU_in_numbers']
            time = form.cleaned_data['Time_in_seconds']
            cmd = '/var/www/lc.sh ' + cpu + ' ' + time
            os.system(cmd)           
            return HttpResponseRedirect('/')
    else:
        form = StressForm()
    return render(request, 'stress.html', {'form': form})

