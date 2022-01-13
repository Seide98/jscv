from django.shortcuts import render
import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django.http import FileResponse
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    now = timezone.now()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(now)

    #contact me form
    if request.method == 'POST':
        personname = request.POST['personname']
        email = request.POST.get('email')
        subject = request.POST['subject']
        if email and subject:
            #send email
            send_mail(
                'Message from ' + personname + ' ' + email, # subject
                subject, # message
                email, # from email
                ['seidee98@gmail.com'], # to email
            )
            print(email)
            return render(request, 'index.html', {'personname': personname})
        else:
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html', {})

def presentation(request):

    return render(request, 'index.html', {})
