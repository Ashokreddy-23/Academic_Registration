from django.urls import path, include
from. import views

urlpatterns = [
    path("checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),
    path("studenthome", views.studenthome, name="studenthome"),
    path("studentchangepw", views.studentchangepw, name="studentchangepw"),
    path("studentupdatepw", views.studentupdatepw, name="studentupdatepw"),
    path("studentcourses", views.studentcourses, name="studentcourses"),
    path("displayscourses", views.displaystudentcourses, name="displaystudentcourses"),
    path("studentcoursecontent", views.studentcoursecontent, name="scoursecontent"),
    path("studentmapcourses", views.studentmapcourses, name="studentmapcourses"),
    path("register",views.register,name="register")

]