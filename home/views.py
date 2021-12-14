from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
#from django.contrib.auth.forms import UserCreationForm
from home.models import Contact,HotelCard
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from math import ceil

# Create your views here.
def home(request):
    allprods=[]
    products= HotelCard.objects.all()
    n= len(products)
    nSlides= n//3 + ceil((n/3) + (n//3))
    # allprods.append([products,range(1,nSlides),nSlides])
    # params = {'allprods':allprods}
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"index.html", params)


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        desc=request.POST['desc']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<5:
            messages.error(request,"Please fill the form correctly.")
        else:
            c= Contact(name=name, phone=phone, email=email,desc=desc)
            c.save()
            messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')

def signup(request):
    if request.method == 'POST':
        #get the parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #check for inputs
        if len(username)>10:
            messages.error(request, "Username is must be under 10 charcters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must contain letters and numbers")
            return redirect('home') 

        if pass1!=pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "your account has been created")

        return redirect('home')
    #return render(request,'register.html')
    else:
        return HttpResponse('404 - Not Allowed')
    
def userlogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse('404 - Not Allowed')

def userLogout(request):
    
    logout(request)
    messages.success(request, "Successfully loged out!!")
    return redirect('home')

    #return HttpResponse('404 - Not Allowed')

def about(request):
    return render(request,'about.html')

