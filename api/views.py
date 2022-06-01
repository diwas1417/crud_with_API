from functools import partial
import imp
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import studentserializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request,pk=None):
    if request.method=='GET':
        
        if pk is not None:
            stu=student.objects.get(pk=pk)
            serializer = studentserializer(stu)
            return Response(serializer.data)


        stu=student.objects.all()
        serializer = studentserializer(stu,many=True)
        return Response(serializer.data)
        
    if request.method=="POST":
        serializer=studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    if request.method=="PUT":
        
        stu=student.objects.get(pk=pk)
        serializer=studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data  update'})
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)  
    
    if request.method=="PATCH":
        
        stu=student.objects.get(pk=pk)
        serializer=studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    if request.method=="DELETE":
        stu=student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'data deleted'})