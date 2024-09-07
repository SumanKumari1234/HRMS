from django.shortcuts import render, redirect
from .models import users
from .models import employee_reg
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from hrmsapp.models import user
from hrmsapp.models import Department


def welcome(request):
    return render(request, 'welcome.html')

def loginpage(request):
    # Establish the database connection
    connection = mysql.connector.connect(host="localhost", user="root", password="Suman@2024", database="Suman")
    cursor = connection.cursor()

    # Fetch email, password, and firstname from the database
    sqlcommand = "SELECT email, pwd, fname, lname FROM loginapp_users"
    cursor.execute(sqlcommand)

    # Initialize lists for storing email, password, and firstname
    e = []
    p = []
    fn = []
    ln = []

    # Append fetched data to lists
    for record in cursor:
        e.append(record[0])
        p.append(record[1])
        fn.append(record[2])
        ln.append(record[3])

    # Close the database connection
    cursor.close()
    connection.close()

    if request.method == "POST":
        email = request.POST['admin_email']
        password = request.POST['admin_password']
        employee_count = employee_reg.objects.count()
        leave_count = user.objects.count()
        department_count=Department.objects.count()
        
        

        i = 0
        k = len(e)
        while i < k:
            if e[i] == email and p[i] == password:
                # If credentials match, render the home page with firstname
                return render(request, 'home.html', {'fname': fn[i], 'lname': ln[i], 'employee_count': employee_count, 'leave_count': leave_count, 'department_count' : department_count})
            
            

            i += 1
        else:
            # If credentials don't match, show an error message
            messages.info(request, "Check Email and Password!")
            return redirect('login')

    return render(request, 'login.html')
    


def register(request):
    if request.method == "POST":
        user= users()

        user.fname = request.POST['first_name']
        user.lname = request.POST['last_name']
        user.email = request.POST['admin_email']
        user.pwd =   request.POST['password']
        user.cpwd = request.POST['confirm_password']

        if user .pwd != (user.cpwd):
            return redirect('register')
        elif user.fname == "" or user.lname == "" or user.email == "" or user.pwd == "" or user.cpwd == "":
            messages.info(request,'Some Fields are Empty')
            return redirect('register')
        else :
            user.save()
    return render(request, 'registration_page.html')


def employeereg(request):
    if request.method == "POST":
        user= employee_reg()

        user.fname = request.POST['employee_first_name']
        user.lname = request.POST['employee_last_name']
        user.email = request.POST['employee_email']
        user.pwd =   request.POST['employee_password']
        user.cpwd = request.POST['employee_confirm_password']

        if user .pwd != (user.cpwd):
            return redirect('employeereg')
        elif user.fname == "" or user.lname == "" or user.email == "" or user.pwd == "" or user.cpwd == "":
            messages.info(request,'Some Fields are Empty')
            return redirect('employeereg')
        else :
            user.save()
    return render(request, 'registration_page.html')

def emploginpage(request):
    # Establish the database connection
    connection = mysql.connector.connect(host="localhost", user="root", password="Suman@2024", database="Suman")
    cursor = connection.cursor()

    # Fetch email, password, and firstname from the database
    sqlcommand = "SELECT email, pwd, fname, lname FROM loginapp_employee_reg"
    cursor.execute(sqlcommand)

    # Initialize lists for storing email, password, and firstname
    e = []
    p = []
    fn = []
    ln = []

    # Append fetched data to lists
    for record in cursor:
        e.append(record[0])
        p.append(record[1])
        fn.append(record[2])
        ln.append(record[3])

    # Close the database connection
    cursor.close()
    connection.close()

    if request.method == "POST":
        email = request.POST['employee_email']
        password = request.POST['employee_password']
        
        

        i = 0
        k = len(e)
        while i < k:
            if e[i] == email and p[i] == password:
                # If credentials match, render the home page with firstname
                return render(request, 'Employeehome.html', {'fname': fn[i], 'lname': ln[i]})
            
            

            i += 1
        else:
            # If credentials don't match, show an error message
            messages.info(request, "Check Email and Password!")
            return redirect('login')

    return render(request, 'login.html')