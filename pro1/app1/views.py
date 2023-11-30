from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password,make_password
from django.http import HttpResponse 
from app1.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'sign-up.html')

def dashboard(request):
    totat_c = Addcourse.objects.count()
    return render(request,'dashboard.html',{"total_c":totat_c})

def courses(request):
    courses = Addcourse.objects.all()
    return render(request,'courses.html',{"courses":courses})

def viewstudents(request):
    student = Addcourse.objects.all()
    student_obj =Addstudent.objects.all()
    return render(request,'viewstudents.html',{"student":student,"student_obj":student_obj})

def ragistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST.get("email")
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
            return redirect('/signup/')
        elif User.objects.filter(password=password).exists():
            messages.error(request,'Password Already Exists')
            return redirect('/signup/')
        else:
            User.objects.create(name=name,email=email,password=password)
            messages.error(request,'Account Successfully Created')
            return redirect('/signup/')
            
def loginform(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(user_password,password):
                return redirect("/dashboard/")
            else:
                messages.error(request,"Password Incorect")
                return redirect('/')
        else:
            messages.error(request,"Email Not Ragistrate")
            return redirect('/')
            
        
def addcourse(request):
    if request.method == 'POST':
        course = request.POST['course']
        fees = request.POST['fees']
        duration = request.POST['duration']
        Addcourse.objects.create(course=course,fees=fees,duration=duration)
        return redirect('/courses/')
    
def delete_c(request,uid):
    data = Addcourse.objects.get(id=uid).delete()
    return render(request,"courses.html",{'data':data})

def addstudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        semail = request.POST['semail']
        smobile = request.POST['smobile']
        saddress = request.POST['saddress']
        scollege = request.POST['scollege']
        sdegree = request.POST['sdegree']
        scourse_id = request.POST.get('scourse')
        total_amount = request.POST['total_amount']
        paid_amount = request.POST['paid_amount']
        due_amount = request.POST['due_amount']
        s_course = Addcourse.objects.get(id=scourse_id)
        if Addstudent.objects.filter(semail=semail).exists():
            messages.error(request,"Email Already Exists")
            return redirect("/viewstudents/")
        else:
            Addstudent.objects.create(sname=sname,semail=semail,smobile=smobile,
            saddress=saddress,scollege=scollege,sdegree=sdegree,scourse=s_course,
            total_amount=total_amount,paid_amount=paid_amount,due_amount=due_amount)
            messages.error(request,"Student Add Successfully")
            return redirect('/viewstudents/')
        

      