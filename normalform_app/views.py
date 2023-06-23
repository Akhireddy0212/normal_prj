from django.http import HttpResponse
from django.shortcuts import render
from .forms import Employe_form
from .models import Employe
# Create your views here.
def Home(request):
    if request.method=='POST':
        form=Employe_form(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            age=request.POST.get('age')
            role=request.POST.get('role')
            salary=request.POST.get('role')
            email=request.POST.get('email')
            z=Employe(name=name,age=age,role=role,salary=salary,email=email)
            z.save()
            return HttpResponse("data added")
        else:
            return HttpResponse("data not added")
    else:
        form=Employe_form() #empty form
        obj={
            'forms':form
        }
    return render(request,'forms.html',obj)