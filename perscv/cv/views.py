from django.shortcuts import render
import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    now = timezone.now()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(now)
    return render(request, 'index.html')