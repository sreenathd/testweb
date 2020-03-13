from django.shortcuts import render
from django import http
from django.shortcuts import render
from django import http
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from forms import StressForm
import os, time

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
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def main(request):
    http_host = request.META['HTTP_HOST']
    host = {'http_host': http_host}
    return render(request, 'index.html', host)

def stress_test(request):
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

