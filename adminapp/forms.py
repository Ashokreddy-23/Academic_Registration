from django import forms

from .models import Faculty, Student
from django import forms
from captcha.fields import CaptchaField

class Myform(forms.Form):
    captcha=CaptchaField()

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"password",}
        labels = {"facultyid":"Enter Faculty ID"}

class AddStudentForm(forms.ModelForm):
            class Meta:
                model = Student
                fields = "__all__"
                exclude = {"password", }
                labels = {"studentid": "Enter Student ID"}


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"studentid"}