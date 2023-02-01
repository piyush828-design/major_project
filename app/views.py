from django.shortcuts import render, redirect,HttpResponse
from  . models import product,seller,buyer
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    pro = product.objects.all()
    slr = seller.objects.all()
    return render(request,'index.html',{'products':pro,'seller':slr})

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        subject = 'welcome to GFG world'
        message = f'Hi {User.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [User.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('/')
        else:
            messages.error(request,"invalid credentials")
            return redirect('/')
   
    return render(request,"login.html")
    
def handleLogout(request):
        logout(request)
        messages.success(request,'successfully logged out')
        return redirect('/')

@login_required
def buy(request,pk):
    print(pk)
    pro = product.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])
        
        by = buyer(name=name,address=address,phone=phone)
        by.save()
        amount = float(pro.price)
        pn = pro.name
        dis = pro.dis
        price = amount
        pro_quantity =quantity
        pro_total = amount*quantity         
        slr = seller.objects.all()
        data = {'pname':pn,'pprice':price,'bname':name,'baddress':address,'bphone':phone,'pdis':dis,'pquantity':pro_quantity, 'ptotal':pro_total}
        
        if len(phone)!=10:
            messages.error(request,'Phone Number must be of 10 digit')
            return redirect('/')
        if not address.isalnum():
            messages.error(request, "Address should contain letters and numbers both")
            return redirect('/')

        return render(request, 'pdf.html', {'data': data, 'seller': slr})

    return render(request, 'buy.html')

def handlecontact(request):
    if request.method == "POST":
        email= request.POST.get('email')
        Name=request.POST.get('Name')
        LastName=request.POST.get("LastName")
     
        city=request.POST.get('city')
        contact=Contact( email=email,city=city,Name=Name,LastName=LastName)
        contact.save()
    return render(request,'home/contact.html')



def pdf(request):
    slr = seller.objects.all()
    return render(request,'pdf.html',{'seller':slr})

def handlemail(request):
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

