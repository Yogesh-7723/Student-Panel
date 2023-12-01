from django.urls import path
from . api import UserList ,CourseList
from . import views

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup),
    path('dashboard/',views.dashboard),
    path('courses/',views.courses),
    path('viewstudents/',views.viewstudents),
    path('ragistration/',views.ragistration),
    path("loginform/",views.loginform),
    path("addcourse/",views.addcourse),
    path("delete/<int:uid>/",views.delete_c ,name="delete"),
    path("addstudent/",views.addstudent),
    path('users/',UserList.as_view()),
    path('course/',CourseList.as_view())

]