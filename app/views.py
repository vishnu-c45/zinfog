from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.


def home(request):
    return render(request,'home.html')


def studentregistration(request):
    if request.method=='POST':
        name = request.POST['name']
        date_of_bitrh = request.POST['dob']
        profile_picture=request.FILES['profile']
        phone_number=request.POST['number']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if Student_Registration.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('studentregistration')
            else:
                user = Student_Registration(name=name,username=username,phonenumber=phone_number,password=password,date_of_birth=date_of_bitrh, profile_pic=profile_picture)
                user.save()
                messages.success(request, 'Registration successfully completed')
                return redirect('studentregistration')
        else:
            messages.info(request, 'password not matching')
            return redirect('studentregistration')
   
    return render(request,'student_registration.html')





def Adminregistration(request):
    if request.method=='POST':
        name = request.POST['name']
        date_of_bitrh = request.POST['dob']
        profile_picture=request.FILES['profile']
        phone_number=request.POST['number']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if Admin_Registration.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('Adminregistration')
            else:
                user = Admin_Registration(name=name,username=username,phonenumber=phone_number,password=password,date_of_birth=date_of_bitrh, profile_pic=profile_picture)
                user.save()
                messages.success(request, 'Registration successfully completed')
                return redirect('Adminregistration')
        else:
            messages.info(request, 'password not matching')
            return redirect('Adminregistration')
   
    return render(request,'Admin.html')


def login_user(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if Student_Registration.objects.filter(username=username,password=password):
            pm=Student_Registration.objects.get(username=username,password=password)
            request.session['st.id']=pm.id
            request.session['sname']=pm.name
            return redirect('student_dash')
        elif Admin_Registration.objects.filter(username=username,password=password):
            am=Admin_Registration.objects.get(username=username,password=password)
            request.session['am.id']=am.id
            request.session['amname']=am.username
            return redirect('Admin_dash')
        else:
            messages.error(request,'user does not exists')
            return redirect('login_user')               
    return render(request,'login.html')

def Admin_dash(request):
    if 'am.id' in request.session:
        students=Student_Registration.objects.all().count()
        admin=request.session['amname']
        return render(request,'admin_dashboard.html',{'students':students,'admin':admin})
    return redirect('login_user')



def addmarks(request):
    if 'am.id' in request.session:
        students=Student_Registration.objects.all()
        if request.method=='POST':
            student_id=request.POST['student']
            maths_mark=request.POST['maths']
            physics_mark=request.POST['phy']
            chemistry_mark=request.POST['che']
            if Student_Mark.objects.filter(student=student_id):
                messages.info(request,'this students mark allready added')
                return redirect('addmarks')
            else:
                
                stm=Student_Mark(student_id=student_id,
                             maths_marks=maths_mark,
                             physics_marks=physics_mark,
                             chemistry_marks=chemistry_mark,
                            )
                stm.save()
                messages.success(request,'successfully created')
                return redirect('addmarks')
        return render(request,'add_marks.html',{'students':students})
    return redirect('login_user')


def student_details(request):
    if 'am.id' in request.session:
        std=Student_Registration.objects.all()
        return render(request,'students_details.html',{'std':std})
    return redirect('login_user')


def admin_viewmarks(request):
    if 'am.id' in request.session:
        std=Student_Mark.objects.all()
        return render(request,'admin_viewmarks.html',{'std':std})
    return redirect('login_user')


def update_studentmarks(request,pk):
    if 'am.id' in request.session:
        std=Student_Mark.objects.get(id=pk)
        if request.method=='POST':
            std.maths_marks=request.POST['maths']
            std.physics_marks=request.POST['phy']
            std.chemistry_marks=request.POST['che']
            std.save()
            return redirect('admin_viewmarks')
        return render(request,'update_mark.html',{'std':std})
    return redirect('login_user')


def Delete_marks(request,pk):
    if 'am.id' in request.session:
        std=Student_Mark.objects.get(id=pk)
        std.delete()
        messages.info(request,'marks deleted successfully')
        return redirect('admin_viewmarks')
    return redirect('login_user')


def student_dash(request):
    if 'st.id' in request.session:
        pk=request.session['st.id']
        student=Student_Registration.objects.get(id=pk)
        return render(request,'student_dashborad.html',{'student':student})
    return redirect('login_user')


def update_student(request):
    if 'st.id' in request.session:
        pk=request.session['st.id']
        std=Student_Registration.objects.get(id=pk)
        if request.method=='POST':
            std.name=request.POST['name2']
            std.phonenumber=request.POST['phn']
            std.age=request.POST['age']
            std.email=request.POST['email']
            std.bio=request.POST['bio']
            std.save()
            return redirect('student_dash')
        return render(request,'update_profile.html',{'std':std})
    return redirect('login_user')


def user_logout(request):
    request.session.flush()
    return redirect('login_user')  

