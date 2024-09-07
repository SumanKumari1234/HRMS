from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user, Department, Designation,Disciplinary
from loginapp.models import employee_reg
from django.http import JsonResponse 
from .models import Events
from django.contrib.auth.models import User

# These are the module views...............

def home(request):
    return render(request,'home.html')

def employeehome(request):
    return render(request,'Employeehome.html')

def leave(request):
    return render(request, 'leave.html')


# Add employee details start here--------------------------------
def addemployeedetails(request):
    return render(request,'Addemployeedetails.html')

def insertuseraddempdet(request):
    vfname = request.POST['firstname'];
    vlname = request.POST['lastname'];
    vemail = request.POST['email'];
    vpwd = request.POST['password'];
    vcpwd = request.POST['confirmpassword'];
    vaddress = request.POST['address'];
    vgender = request.POST['gender'];
    vdesignation = request.POST['designation'];
    vdepartment = request.POST['department'];
    vbloodgroup = request.POST['bloodgroup'];
    vdoj = request.POST['dateofjoining'];
    vpnumber = request.POST['phonenumber'];
    iuaep = employee_reg(fname=vfname, lname=vlname,email=vemail,pwd=vpwd,cpwd=vcpwd,department=vdepartment,
              address=vaddress, gender=vgender, designation=vdesignation, bloodgroup=vbloodgroup,
              doj = vdoj, pnumber = vpnumber);
    iuaep.save();
    return render(request, 'Addemployeedetails.html')

def viewaddemployeedetails(request):
    show = employee_reg.objects.all()
    return render(request, "viewaddemployeedetails.html", {'addempdetdata' : show})
    
def addemployeedetailsdelete(request, id):
    dept = employee_reg.objects.get(email=id)
    dept.delete()
    return redirect("/viewaddemployeedetails")
#------------Add employee details ends here-------------#




#-------Department Details---------------#
def department(request):
    return render(request, 'Department.html')

def viewdepartments(request):
    show = Department.objects.all()
    return render(request, "Viewdepartments.html", {'deptdata' : show}) 

def viewdepartmentsemployee(request):
    show = Department.objects.all()
    return render(request, "Viewdepartmentemployee.html", {'deptdata' : show})

def insertuserdepartment(request):
    vdepartment_name = request.POST['department_name'];
    vdepartment_code= request.POST['department_code'];
    vdepartment_head = request.POST['department_head'];
    vdepartment_description = request.POST['department_description'];


    esdept = Department(department_name=vdepartment_name, department_code=vdepartment_code,department_head=vdepartment_head,department_description=vdepartment_description,);
    esdept.save();
    return render(request, 'Department.html')


def departmentdelete(request, id):
    dept = Department.objects.get(department_name=id)
    dept.delete()
    return redirect("/viewdepartment")
#-----------------Department Details Ends here---------------#





#----------------Designation Starts here-------------------#
def insertdesignation(request):
    vdesignation_title = request.POST['designation_title'];
    vdesignation_code= request.POST['designation_code'];
    vdesignation_head = request.POST['designation_head'];
    vdesignation_description = request.POST['designation_description'];


    desdept = Designation(designation_title= vdesignation_title, designation_code = vdesignation_code,designation_head=vdesignation_head,designation_description=vdesignation_description,);
    desdept.save();
    return render(request, 'Designation.html')


def designation(request):
    return render(request, 'Designation.html')

#-------------------------------Designation ends here--------------------------------------------------------------#

#----------------------------Disicplinary start here -----------------------------------------------#

def disciplinary(request):
    return render(request, 'Disciplinary.html')

def insertdisciplinary(request):
    vemployee_name = request.POST['employee_name'];
    vemployee_code= request.POST['employee_code'];
    vdisciplinary_action = request.POST['disciplinary_action'];
    vdate_of_action = request.POST['date_of_action'];
    vdis_notes = request.POST['disciplinary_notes'];

    dis = Disciplinary(employee_name= vemployee_name, employee_code = vemployee_code,disciplinary_action=vdisciplinary_action,
                          date_of_action=vdate_of_action, disciplinary_notes=vdis_notes);
    dis.save();
    return render(request, 'Disciplinary.html')



#---------------Disciplinary--End here----------------------------------------#


def holiday(request):
    return render(request, 'Holiday.html')

def login(request):
    return render(request, 'login.html')

def inactive(request):
    return render(request, 'inactive.html')


# Leave application and View leave application   ------------

def userreg(request):
    return render(request, 'Userreg.html')

def usersettingpage(request):
    return render(request, 'Usersettingpage.html')

def insertuser(request):
    veid = request.POST['empid'];
    vefirstname = request.POST['empname'];
    velastname = request.POST['emplastname'];
    vedepartment = request.POST['empdepartment'];
    vedesignation = request.POST['empdesignation'];
    vleavetype = request.POST['typeofleave'];
    vecontact = request.POST['empcontact'];
    vnoofdays = request.POST['noofdays'];
    vfromdate = request.POST['fromdate'];
    vtodate = request.POST['todate'];
    vapplieddate = request.POST['submitteddate'];
    vattachfile = request.POST['attachfile'];
    vdescription = request.POST['description']
    es = user(eid=veid, efirstname=vefirstname,elastname=velastname,edepartment=vedepartment,
              edesignation=vedesignation, leavetype=vleavetype, econtact=vecontact, noofdays=vnoofdays,
              fromdate = vfromdate, todate = vtodate, submitteddate = vapplieddate, uploadfile = vattachfile, 
              description = vdescription);
    es.save();
    return render(request, 'userreg.html') 

def viewusers(request):
    users = user.objects.all()
    return render(request, "viewusers.html", {'userdata' : users})

def deleteprofile(request, id):
    us = user.objects.get(eid=id)
    us.delete()
    return redirect("/viewusers")

# Leave application and View leave application ends here   ------------






# Event and calendar  -----------

def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

    #Event and calendar ends here---------





