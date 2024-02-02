from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

@api_view(['GET'])
def getall(request):
    stdata=Task.objects.all()
    serial=taskserial(stdata,many=True)
    return Response(data=serial.data)

@api_view(['POST'])
def insertdata(request):
    if request.method=="POST":
       serialdata= taskserial(data=request.data)
       if serialdata.is_valid():
           serialdata.save()
           return Response(status=status.HTTP_202_ACCEPTED)
       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['PUT','GET'])
def updatedata(request,id):
      try:
        stid=Task.objects.get(id=id)
      except Task.DoesNotExist:
          return Response(status=status.HTTP_400_BAD_REQUEST)
      
      if request.method=="GET":
          serial=taskserial(stid)
          return Response(data=serial.data)
      
      if request.method=="PUT":
          serial=taskserial(data=request.data,instance=stid)
          if serial.is_valid():
              serial.save()
              return Response(status=status.HTTP_202_ACCEPTED)
          else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
          

@api_view(["DELETE",'GET'])
def deletedata(request,id):
    try:
        stid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="GET":
        serial=taskserial(stid)
        return Response(data=serial.data)
    
    if request.method=="DELETE":
        Task.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
def index(request):
    url="http://127.0.0.1:8000/"
    rk=requests.get(url)
    data=rk.json()
    return render(request,"index.html",{'data':data})