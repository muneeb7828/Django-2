
# Create your views here.
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


def home(request):
    return render(request,'index.html')



@api_view(['GET','POST','PUT','PATCH','DELETE'])
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
        return Response("course create successfully")
 

    elif(request.method == "PUT" or request.method == "PATCH"):
        if not id:
            return Response({"message":"id is required"})
        
        course = Course.objects.filter(id=id)              # ye where clause ki tarah hota he aur ye filter method se hi hota he kyuki ye hi update method return karta he get nahi karta aur ye update ke sath aur bhi method return karta he

        if not course.exists():                            # ye method check karta he data he ke nahi
             return Response({"message":"Course not found"})
        
        course.update(**request.data)
        return Response("course updated successfully")


# nested serializer



