
# Create your views here.
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializer import *


def home(request):
    return render(request,'index.html')



@api_view(['GET','POST','PUT','PATCH','DELETE',"OPTIONS"])
def course_view(request,id=None):                          # ye default parameter diya he
    if(request.method == "GET"):
        courses=Course.objects.all()                       # isse jitne bhi instance bane hote he vo sab ajate he
        serializers=courseSerializer(courses,many=True)    # ye json format me convert kardeta he aur many=True taki ek se zada data bhi rakh sake
        return Response(serializers.data)                  # isme jo bhi likhte vo thunder client ke response pe show hota he
 
    elif(request.method == "DELETE"):
        course=Course.objects.get(id=id)  
        course.delete()  
        return Response('delete')

    elif(request.method == "POST"):                        # aur jab bhi post ya update karte he to thunder client ke body ya form me data likhne ke baad karte he
        Course.objects.create(**request.data)              # **request.data ye esa isliye likha he taki iske function me bhi esa likha he aur jo data he ye thunder client ke body ya form me data likhte he ye usko leta he
        print(request.data,'muneeb')
        return Response("course create successfully")
 

    elif(request.method == "PUT" or request.method == "PATCH"):
        if not id:
            return Response({"message":"id is required"})
        
        course = Course.objects.filter(id=id)              # ye where clause ki tarah hota he aur ye filter method se hi hota he kyuki ye hi update method return karta he get nahi karta aur ye update ke sath aur bhi method return karta he
        print(course)
        if not course.exists():                            # ye method check karta he data he ke nahi
             return Response({"message":"Course not found"})
        
        course.update(**request.data)                      # ye change kar deta he object ko
        return Response("course updated successfully")
    
    elif(request.method == "OPTIONS"):
        if not id:
           return Response({"message":"id is required"}) 
        try:
         course=Course.objects.get(id=id)
        except:
             return Response({"message":"Course not found"})            
        serializers=courseSerializer(course)

        return Response(serializers.data)


@api_view(['GET','POST','PUT','PATCH','DELETE',"OPTIONS"])
def lesson_view(request,id=None):
    if(request.method == "GET"):
        lesson=Lesson.objects.all() 
        serializers=lessonSerializer(lesson,many=True) 
        return Response(serializers.data) 

    elif(request.method == "DELETE"):
        lesson=Course.objects.get(id=id)  
        lesson.delete()  
        return Response('delete')    

    elif(request.method == "POST"):                        
        Lesson.objects.create(**request.data)              
        print(request.data,'muneeb')
        return Response("lesson create successfully")
    
    elif(request.method == "PUT" or request.method == "PATCH"):
        if not id:
            return Response({"message":"id is required"}) 
        
        course = Course.objects.filter(id=id)             
        print(course)
        if not course.exists():                           
             return Response({"message":"lesson not found"})
        
        lesson.update(**request.data)            
        return Response("lesson updated successfully")




@api_view(['GET','POST','PUT','PATCH','DELETE',"OPTIONS"])
def department_view(request,id=None):
    if(request.method == "GET"):
        department=Department.objects.all() 
        serializers=DepartmentSerializer(department,many=True) 
        return Response(serializers.data) 

    elif(request.method == "DELETE"):
        department=Department.objects.get(dep=id)  
        department.delete()  
        return Response('delete')    

    elif(request.method == "POST"):                        
        Department.objects.create(**request.data)              
        print(request.data,'muneeb')
        return Response("department create successfully")
    
    elif(request.method == "PUT" or request.method == "PATCH"):
        if not id:
            return Response({"message":"id is required"}) 
        
        course = Department.objects.filter(id=id)             
        print(course)
        if not course.exists():                           
             return Response({"message":"department not found"})
        
        department.update(**request.data)            
        return Response("department updated successfully")




@api_view(['GET','POST','PUT','PATCH','DELETE',"OPTIONS"])
def employee_view(request,id=None):
    if(request.method == "GET"):
        employee=Employee.objects.all() 
        serializers=EmployeeSerializer(employee,many=True) 
        return Response(serializers.data) 

    elif(request.method == "DELETE"):
        employee=Employee.objects.get(id=id)  
        employee.delete()  
        return Response('delete')    

    elif(request.method == "POST"):                        
        print(request.data,'muneebsssssss')
        employee=Employee.objects.create(**request.data)  
                   
        return Response("employee create successfully")
    
    elif(request.method == "PUT" or request.method == "PATCH"):
        if not id:
            return Response({"message":"id is required"}) 
        
        course = Employee.objects.filter(id=id)             
        print(course)
        if not course.exists():                           
             return Response({"message":"employee not found"})
        
        employee.update(**request.data)            
        return Response("employee updated successfully")























# nested serializer

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer


