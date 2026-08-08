from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course,Studentcourses

from facultyapp.models import CourseContent



# Create your views here.
def studenthome(request):
    sid=request.session["sid"]
    student= Student.objects.get(studentid=sid)
    print(student)
    return render(request,"studenthome.html",{"sid":sid,"student":student})


def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["sid"] = sid  #creating a session
        student = Student.objects.get(studentid=sid)
        print(student)
        return render(request,"studenthome.html",{"sid":sid,"student":student})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("login failed ")

def studentchangepw(request):
    sid = request.session["sid"]
    return render(request,"studentchangepw.html",{"sid":sid})


def studentupdatepw(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old pw is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated...")
        msg = "password updated"
    else:
        print("old pw is wrong")
        msg = "old password wrong"

    return render(request,"studentchangepw.html",{"sid":sid,"message":msg})


def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid = request.session["sid"]
    content = CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})

def displaystudentcourses(request):
    sid=request.session["sid"]
    Ayear= request.POST["Ayear"]
    semester = request.POST["semester"]

    courses =Course.objects.filter(Q(academicyear=Ayear)&Q(semester=semester))

    return render(request,"displaystudentcourses.html",{"courses":courses})


def studentmapcourses(request):
    sid = request.session["sid"]
    fcourses = Studentcourses.objects.all()
    print(fcourses)
    return render(request,"studentmapcourses.html",{"sid":sid,"fcourses":fcourses})

def register(request):
    return  render(request,"register.html")