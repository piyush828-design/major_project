from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == 'POST':
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub,msg,email)
        send_mail(
            sub,msg,'piyushpawar171@gmail.com',
            [email]
        )
        return HttpResponse('email has been sent')
    return render(request,'mailsender/mail.html')