# myapp/views.py
from rest_framework import generics
from .models import Book
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def insertdata(request):
    if request.method=="POST":
        serial=BookSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])     
def getall(request):
    alldata=Book.objects.all()
    serial=BookSerializer(alldata,many=True)
    return Response(data=serial.data)


@api_view(['GET','DELETE'])
def deletedata(request,id):
    try:
        bid=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serial=BookSerializer(bid)
        return Response(data=serial.data)
    
    if request.method=="DELETE":
        Book.delete(bid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
@api_view(['PUT','GET'])
def updatedata(request,id):
      try:
        stid=Book.objects.get(id=id)
      except Book.DoesNotExist:
          return Response(status=status.HTTP_400_BAD_REQUEST)
      
      if request.method=="GET":
          serial=BookSerializer(stid)
          return Response(data=serial.data)
      
      if request.method=="PUT":
          serial=BookSerializer(data=request.data,instance=stid)
          if serial.is_valid():
              serial.save()
              return Response(status=status.HTTP_202_ACCEPTED)
          else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


