

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

]












