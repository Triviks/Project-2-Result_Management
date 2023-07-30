from django.shortcuts import render, redirect
from django.contrib import messages
from .models import profile, result
from django.contrib.auth.models import User, auth


# Create your views here.
def dashboard(request):
    return render(request,"Dashboard_Portal.html")
def Admin(request):
  if request.method=="POST":
         username=request.POST["username"]
         password=request.POST["password"]
         email=request.POST["email"]
         user = auth.authenticate(username=username,password=password,email=email)
         if user is not None:
              auth.login(request,user)
              context={}
              dest=profile.objects.get(name=request.user.username)
              context["dest"]=dest
              return render(request,"Admin.html",context)
         else:
              messages.info(request,'Invalid credentials')
              return redirect('dashboard')
  else:     
       return render(request,"Dashboard_Portal.html") 
    # if register==201241101058 and email=="sudhakaransneha30@gmail.com" and password==123:
    #     dests=profile.objects.all()
    #     return render(request,"Admin.html",{"dests":dests}) 
    # else:
    #     return render(request,"dashboard_Portal.html")
def  persona(request):
      context={}
      dest=profile.objects.get(name=request.user.username)
      context["dest"]=dest
      return render(request,"Admin.html",context)
def exam(request):
     return render(request,"Exam_schedule.html")  
def result1(request):
     context={}
     dest=result.objects.get(name=request.user.username)
     context["dest1"]=dest
     return render(request,"Result.html",context)
    #      else:
    #           messages.info(request,'Invalid credentials')
    #           return redirect('dashboard')
    # else:     
    #     return render(request,"dashboard.html") 
    # dest=result.objects.all.order_by("name")
    # return render(request,"Result.html",{"dest1":dest})

def downloading(request):
    return render(request,"answer_sheets.html")