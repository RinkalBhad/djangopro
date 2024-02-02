from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializer import*
import requests

@api_view(['GET'])
def getall(request):
    stdata=student.objects.all()
    v=studentserializer(stdata,many=True)
    return Response(data=v.data)


@api_view(['GET'])
def getid(request,id):
    try:
        v=student.objects.get(id=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    ss=studentserializer(v)
    return Response(data=ss.data)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stdata=student.objects.get(id=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serial=studentserializer(stdata)
        return Response(data=serial.data)

    if request.method=='DELETE':
        student.delete(stdata)
        return Response(status=status.HTTP_202_ACCEPTED)
    


@api_view(['POST'])
def savedata(request):
    if request.method=="POST":
        serail=studentserializer(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stdata=student.objects.get(id=id)

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serial=studentserializer(stdata)
        return Response(data=serial.data)
    
    if request.method=="PUT":
        ss=studentserializer(data=request.data,instance=stdata)
        if ss.is_valid():
            ss.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
def home(request):
    url="http://127.0.0.1:8000/"
    rk=requests.get(url)
    stdata=rk.json()
    return render(request,"home.html",{'stdata':stdata})