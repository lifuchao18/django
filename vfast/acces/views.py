#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from acces.models import Students
from acces.forms import StudentForm
from django.core.urlresolvers import reverse
import datetime
# Create your views here.

def index(request):
    return HttpResponse("My Django!")

def html(request):
    return render(request,"acces/index.html")

def server(request):
    server_list=[
    "192.168.116.1",
    "192.168.116.2",
    "192.168.116.3",
    "192.168.116.4",
    "192.168.116.5",
    ]
    return render(request,"acces/index2.html",context={"server_list":server_list})

def student(request):
    data = [
        {'name':"张三",'age':"18",'mobile':"123123121"},
        {'name':"李四",'age':"19",'mobile':"123123112"},
        {'name':"王五",'age':"17",'mobile':"123456123"}
    ]
    title = 'Django First day'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    return render(request,'acces/index3.html',locals())

def studens(request):
    data = []
    for s in Students.objects.all():
      inf = {}
      inf['name'] = s.name
      inf['age'] = s.age
      inf['mobile'] = s.mobile
      data.append(inf)
    title = 'Django Second day'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    return render(request,'acces/index4.html',locals())

def students(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           age = form.cleaned_data['age']
           gender = form.cleaned_data['gender']
           mobile = form.cleaned_data['mobile']
           height = form.cleaned_data['height']
           weight = form.cleaned_data['weight']
           Students.objects.create(name=name,age=age,gender=gender,mobile=mobile,height=height,weight=weight)
           return HttpResponseRedirect(reverse('students'))
    data = Students.objects.all()
    return render(request,'acces/index4.html',locals())
    

def studens_info(request,_id):
    name = request.GET.get('name',0)
    s = int(name) +int( _id)
    return HttpResponse(s)


def delete_student(request,_id):
    try:
        student = Students.objects.get(pk=_id).delete()
    except Students.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('students'))


def student_info(request,_id):
    try:
        student = Students.objects.get(pk=_id)
    except Students.DoesNotExist:
        return HttpResponseRedirect(reverse('students'))
    if request.method == 'POST':
        print request.POST
        for key,value in request.POST.iteritems():
            print key,value
            if value and hasattr(student,key):
                setattr(student,key,value)
        student.save()
        return HttpResponseRedirect(reverse('students'))
    return render(request,'acces/index5.html',context={'student':student}) 
