from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from employee.models import *

# Create your views here.
def hello(request):

    return render(request, 'index.html')
# To display all emp details
def All_emp(request):
    emps=Employee.objects.all()
    role=Role.objects.all()
    dept=Department.objects.all()
    context={'emps': emps,'role':role,'dept':dept}
    return render(request, 'All_emp.html', context)

# Adding a emp in database

def Add_emp(request):
    RAO=Role.objects.all()
    DO=Department.objects.all()
    
    if request.method == 'POST':
        
        first_name = request.POST['emp_first_name'] 
        last_name = request.POST['emp_last_name']
        dept =  request.POST['dept'] 
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']
        
        DE=Department.objects.get(id=dept)
        ROL=Role.objects.get(id=role)
        
        EDO=Employee.objects.get_or_create(emp_first_name=first_name,emp_last_name=last_name,dept=DE,salary=salary,
                                           bonus=bonus,role=ROL,phone=phone,hire_date=datetime.now())
        
        return render(request, 'index.html')
    return render(request,'Add_emp.html',{'RAO':RAO,'DO':DO})

 # Removing an emp from database
def Remove_emp(request):

    emps=Employee.objects.all()
    context = {'emps': emps}
    if request.method=='POST':
        rem=request.POST['rem']
        RO=Employee.objects.filter(id=rem).delete()
        return render(request, 'index.html')
    return render(request, 'Remove_emp.html', context)
    
# Editing emp details
def Filter_emp(request):
    if request.method == 'POST':
        name = request.POST['emp_first_name']
        dept = request.POST['dept']
        role = request.POST['role']
        #emps = Employee.objects.all()
        userValues={
            'name':name,
            'dept':dept,
            'role':role,
           
        }

        error_msg=None
        success_msg=None
        if name:
            emps = Employee.objects.filter(Q(emp_first_name = name) | Q(emp_last_name = name),dept__name=dept,role__position=role,)
            success_msg='matching records found..!'
            
        if  (not name) or (not dept) or (not role):
            error_msg='* Should Not Be Empty '
            d={'error':error_msg,'value':userValues}
            return render(request,'Filter_emp.html',d)

        if not emps.exists():
            error_msg='No matching records found..!'
            d={'error':error_msg,'value':userValues}
            return render(request,'Filter_emp.html',d)
            #return HttpResponse('No matching records found')

        return render(request, 'All_emp.html', {'emps': emps,'success':success_msg,'value':userValues})
    
    return render(request, 'Filter_emp.html')

