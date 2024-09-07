from django.urls import path
from . views import home , leave, department,viewdepartments,insertdisciplinary,addemployeedetailsdelete,viewaddemployeedetails,viewdepartmentsemployee,insertuserdepartment,insertuseraddempdet, designation,disciplinary, holiday, login, inactive, userreg, insertuser, viewusers, deleteprofile, usersettingpage
from django.contrib.auth import views as auth_views
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home, name='home'),
    path('employeehome/', views.employeehome, name='employeehome'),
    path('addemployeedetails/', views.addemployeedetails, name='addemployeedetails'),
    path('insertuseraddempdet/', views.insertuseraddempdet, name='insertuseraddempdet'),
    path('viewaddemployeedetails/', views.viewaddemployeedetails, name='viewaddemployeedetails'),
    path('addemployeedetailsdelete/<str:id>', views.addemployeedetailsdelete,name='addemployeedetailsdelete'),
    path('disciplinary/', views.disciplinary, name='disciplinary'),
    path('insertdisciplinary/', views.insertdisciplinary, name='insertdisciplinary'),
    path('department/', views.department, name='department'),
    path('viewdepartment/',views.viewdepartments,name ='viewdepartment'),
    path('viewdepartmentemployee/',views.viewdepartmentsemployee,name ='viewdepartmentemployee'),
    path('departmentdelete/<str:id>', views.departmentdelete,name='departmentdelete'),
    path('designation/', views.designation, name='designation'),
    path('disciplinary/', views.disciplinary, name='disciplinary'),
    path('holiday/', views.holiday, name='holiday'),
    path('login/', views.login, name='login'),
    path('usersettingpage/', views.usersettingpage, name='usersettingpage'),
    path('inactive/', views.inactive, name='inactive'),
    path('userreg/', views.userreg, name='userreg'),
    path('insertuser/', views.insertuser, name='insertuser'),
    path('insertuserdepartment/', views.insertuserdepartment, name='insertuserdepartment'),
    path('insertdesignation/', views.insertdesignation, name='insertdesignation'),
    path('viewusers/', views.viewusers, name='viewusers'),
    path('deleteprofile/<int:id>', views.deleteprofile,name='deleteprofile'),
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)