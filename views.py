from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from Application.models import Login
from django.contrib import messages
from Application.models import ContactModel
from Application.models import MeritModel
from Application.models import AthleticModel
from Application.models import EconomicalModel
from Application.models import Merit_Services
from Application.models import Sport_Services
from Application.models import Economical_Services

# Create your views here.
def index(request):
    return redirect("/Login")

def Home(request):
    if request.user.is_anonymous:
        return redirect("/Login")
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def Contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=ContactModel(name=name, email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Your Message has been sent")
    return render(request, 'Contact.html')

def Merit(request):
    if request.method == "POST":
        sname=request.POST.get('sname')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        semail=request.POST.get('semail')
        age=request.POST.get('age')
        caste=request.POST.get('caste')
        sphone=request.POST.get('sphone')
        sclname=request.POST.get('sclname')
        marks1=request.POST.get('marks1')
        clgname=request.POST.get('clgname')
        marks2=request.POST.get('marks2')
        marks3=request.POST.get('marks3')
        emrank=request.POST.get('emrank')
        merit=MeritModel(sname=sname, fname=fname, mname=mname, semail=semail,age=age,caste=caste,sphone=sphone,sclname=sclname,marks1=marks1,clgname=clgname, marks2=marks2,marks3=marks3,emrank=emrank)
        merit.save()
        messages.success(request, "Your Form has been submitted")
        return redirect("/Meritservice")
    return render(request, 'Merit.html')

def Athletic(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        semail = request.POST.get('semail')
        age = request.POST.get('age')
        caste = request.POST.get('caste')
        sphone = request.POST.get('sphone')
        sport = request.POST.get('sport')
        academy = request.POST.get('academy')
        authority = request.POST.get('authority')
        level = request.POST.get('level')
        disabilities = request.POST.get('disabilities')

        athletic_model = AthleticModel(
            sname=sname,
            fname=fname,
            mname=mname,
            semail=semail,
            age=age,
            caste=caste,
            sphone=sphone,
            sport=sport,
            academy=academy,
            authority=authority,
            level=level,
            disabilities=disabilities
        )
        athletic_model.save()

        messages.success(request, "Your form has been submitted")
        return redirect("/Sportservice")
    return render(request, 'Athletic.html')

def Economical(request):
    if request.method == "POST":
        sname=request.POST.get('sname')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        focc=request.POST.get('foccupation')
        mocc=request.POST.get('moccupation')
        email=request.POST.get('email')
        age=request.POST.get('age')
        caste=request.POST.get('caste')
        phone=request.POST.get('phone')
        sclname=request.POST.get('sclname')
        clgname=request.POST.get('clgname')
        income=request.POST.get('income')
        economical=EconomicalModel(sname=sname, fname=fname, mname=mname,focc=focc,mocc=mocc,email=email,age=age,caste=caste,phone=phone,sclname=sclname,clgname=clgname,income=income)
        economical.save()
        messages.success(request, "Your Form has been submitted")
        return redirect("/Economicalservice")
    return render(request, 'Economical.html')

def Login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        user.save()
        messages.success(request, "Your Login was Successfull")
        if user is not None:
            login(request,user)
            return redirect("/Home")
        else:
            return render(request, 'Login.html')
    return render(request, 'Login.html')
def LogoutUser(request):
    logout(request) 
    return redirect("/Login")

def Mservice(request):
    merit_data=Merit_Services.objects.all()
    data={
        'merit_data':merit_data
    }
    return render(request, 'Merit_Service.html',data)

def Sservice(request):
    sport_data=Sport_Services.objects.all()
    data1={
         'sport_data':sport_data
    }
    return render(request, 'Sport_Service.html',data1)

def Eservice(request):
    ews_data=Economical_Services.objects.all()
    data2={
        'ews_data':ews_data
    }
    return render(request, 'Economical_Service.html',data2)