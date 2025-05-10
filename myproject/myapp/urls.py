

from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('course/',course_view),
    path('course/<int:id>/',course_view),

]












