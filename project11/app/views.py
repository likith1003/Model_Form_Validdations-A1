from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    ERFO = RegisterForm()
    d = {'ERFO': ERFO}
    if request.method == 'POST':
        RFDO = RegisterForm(request.POST)
        if RFDO.is_valid():

            RFDO.save()
            return HttpResponse('Done..')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)