

from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('course/',course_view),
    path('course/<int:id>/',course_view),
    path('lesson/',lesson_view),
    path('lesson/<int:id>/',lesson_view),
    path('department/',department_view),             
    path('department/<int:id>/',department_view),    
    path('employee/',employee_view),
    path('employee/<int:id>/',employee_view),
    path('signup',register_view,),
    path('login',login_user),
    path('logout',logout_user),
    path('user/',User_database),
    path('user/<str:username>/',User_database),         # iska datatype bhi change kar sakte he int bhi rakh sakte he aur str bhi rakh sakte he aur iske argument me vohi naam aayega jo parameter me diya he

]
 

# superuser
# {
# "usernam":"sami12",
# "passwrd":"Samidjango@12345"
# }

# {
# "usernam":"muneeb123",
# "passwrd":"Muneebdjango@12345"
# }


# siqnup
# {
# "usernam":"rehman123",
# "passwrd":"Muneebdjango@12345"
# }

# {
# "usernam":"hamza123",
# "passwrd":"hamzadjango@12345"
# }

# {
# "usernam":"abdurrehman123",
# "passwrd":"abdurrehmandjango@12345"
# }

# superuser 
# {
# "usernam":"muneeb",
# "passwrd":"Muneebdjango@12345"
# }








