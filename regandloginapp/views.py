from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Reg
from .forms import RegForm,LoginForm

def reg(request):
    if request.method=="POST":
        forms=RegForm(request.POST)
        if forms.is_valid():
            fname = request.POST.get('fname','')
            lname = request.POST.get('lname', '')
            user = request.POST.get('user', '')
            pwd = request.POST.get('pwd', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            dob = request.POST.get('dob', '')
            gender = request.POST.get('gender', '')
            reg = Reg(fname=fname,lname=lname,user=user,pwd=pwd,mobile=mobile,email=email,dob=dob,gender=gender)
            reg.save()
            return HttpResponse('reg success')

    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})

def login(request):
    if request.method=="POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            user=MyLoginForm.cleaned_data['user']
            pwd = MyLoginForm.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=user)
            dbpwd=Reg.objects.filter(pwd=pwd)
            if not dbuser or dbpwd:
                return HttpResponse('login success')
            else:
                return HttpResponse('login failed')
        else:
            print(MyLoginForm.errors)
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
def home(request):
    return render(request,'home.html')

