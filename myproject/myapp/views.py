
# Create your views here.
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializer import *
from django.contrib.auth.models import User                 # ye jo admin pe user he vo import kiya he
from django.contrib.auth import authenticate,login,logout   # ye function user ko authenticate karne ke liye aur login or logout karne ke liye hota he

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
        
        lesson = Lesson.objects.filter(id=id)             
        print(lesson)
        if not lesson.exists():                           
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
        
        department = Department.objects.filter(dep=id)             
        print(department,'muneeb')
        if not department.exists():                           
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


@api_view(['POST'])
def register_view(request):                                     # ye tabhi chalega jab request method post hoga
    usernam= request.data.get('usernam')                        # signup jab is path pe jate he usme jo content me jo likha hota he data me vo ata he 
    passwrd= request.data.get('passwrd')

    if User.objects.filter(username=usernam).exists():          # is User me jitne bhi user bane hote he vo sab user ke object (data) ajate he matlab ke ye jo User he ye database hi he jese Course model database he jisme sare object (data) hote he
       return Response({'message':'username already exists'})   # exists method tab true return karta he jab isme kuch hota he

    else:
       User.objects.create_user(username=usernam, password=passwrd)   # isse create hoke save bhi ho jata he database me
       return Response({'message':'user registered successfully'})


@api_view(['POST'])
def login_user(request):
    usernam= request.data.get('usernam')
    passwrd= request.data.get('passwrd')
    user=authenticate(username=usernam,password=passwrd)          # ye sahi ho to hi return karta he nahi to None return karta he
    if user is not None:
       return Response({'message':'login successful'})
    else:
      return Response({'message':'Invalid credentials'})


@api_view(['POST'])
def logout_user(request):
    print(request.POST,'muneeebssssss')
    logout(request)                                                # is method se logout ho jate he
    return Response({'message':'logout successful'})


# create crud of User


@api_view(['GET','POST','PUT','PATCH','DELETE',"OPTIONS"])
def User_database(request,username=None):
    if(request.method == "GET"):
        user=User.objects.all() 
        serializers=UserSerializer(user,many=True) 
        return Response(serializers.data) 

    elif(request.method == "DELETE"):
        user=User.objects.get(username=username)  
        user.delete()  
        return Response('delete')    

    elif(request.method == "POST"):                        
        User.objects.create(**request.data)              
        print(request.data,'muneeb')
        return Response("user create successfully")
    
    elif(request.method == "PUT" or request.method == "PATCH"):
        if not username:
            return Response({"message":"username is required"}) 
        
        user = User.objects.filter(username=username)             
        print(user,'muneeb')
        if not user.exists():                           
             return Response({"message":"user not found"})
        
        user.update(**request.data)            
        return Response("user updated successfully")


    elif(request.method == "OPTIONS"):
        if not username:
           return Response({"message":"username is required"}) 
        try:
         user=User.objects.get(username=username)
        except:
             return Response({"message":"user not found"})            
        serializers=UserSerializer(user)

        return Response(serializers.data)












class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer


