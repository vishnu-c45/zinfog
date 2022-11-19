from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('studentreister/',studentregistration,name='studentregistration'),
    path('Adminregistration/',Adminregistration,name='Adminregistration'),
    path('admindash/',Admin_dash,name='Admin_dash'),
    path('login_user/',login_user,name='login_user'),
    path('student/',student_dash,name='student_dash'),
    path('user_logout/',user_logout,name='user_logout'),
    path('add_marks/',addmarks,name='addmarks'),
    path('student_details/',student_details,name='student_details'),
    path('admin_viewmarks/',admin_viewmarks,name='admin_viewmarks'),
    path('update_studentmarks/<int:pk>/',update_studentmarks,name='update_studentmarks'),
    path('Delete_marks/<int:pk>/',Delete_marks,name='Delete_marks'),
    path('update_student/',update_student,name='update_student'),
    
]
