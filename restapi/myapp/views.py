
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
    stdata=userdata.objects.all()
    serial=userserializer(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
      stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=userserializer(stid)
    return Response(data=serial.data)



@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=userserializer(stid)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        userdata.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        stdata=userserializer(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=userserializer(stid)
        return Response(data=serial.data)

    if request.method=='PUT':
        stdata=userserializer(data=request.data,instance=stid)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
def home(request):
    url="http://127.0.0.1:8000/"
    req=requests.get(url)
    data=req.json()
    return render(request,'home.html',{'data':data})


def another(request):
    url="https://restcountries.com/v3.1/all"
    rk=requests.get(url)
    data=rk.json()
    return render(request,"another.html",{"data":data})


    


    base_url = "https://restcountries.com/v3.1/name/"
    url = f"{base_url}{country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        country_data = response.json()
        return country_data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

