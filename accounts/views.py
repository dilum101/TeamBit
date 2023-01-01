

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Reg_Users,Unreg_Users,Training_Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import Reg_Users_Serializer,Training_Session_Serializer
import json
from .serializers import Reg_Users_Serializer


@api_view(['POST'])
def Register(request):
   
   
   if(request.method== 'POST'):
  
        
            Fname = request.POST.get('firstName')
            Lname = request.POST.get('lastName')
            User_name = Fname+"_"+Lname;
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            
            
            if Unreg_Users.objects.filter(email = Email).exists():
               
            
                  if Reg_Users.objects.filter(user_name = User_name).exists():
                     return Response("User_Name already Exists", status=status.HTTP_406_NOT_ACCEPTABLE)
                  elif Reg_Users.objects.filter(email = Email).exists():
                     return Response("Email already Exists", status=status.HTTP_406_NOT_ACCEPTABLE)
                  else:
                     
                     User = Reg_Users.objects.create(user_name = User_name,email_id = Email,password = Password)
                     if User is not None:
                        serializer = Reg_Users_Serializer(User)
                        
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                     else:
                        return Response("Error: Useer Not Registered !",status=status.HTTP_409_CONFLICT)
               
            else:
               return Response("Un-autherized Email",status=status.HTTP_401_UNAUTHORIZED)
         
                 
   

@api_view(['POST'])
def Login(request):
   
   print("Request Arrived ***********")
   
   if request.method == 'POST':
      print(request)
      email = request.POST.get("email")
      password = request.POST.get("password")

      print("User Details: "+email+password)

      if Reg_Users.objects.filter(email=email).exists():
         user  = Reg_Users.objects.filter(email=email).values()
         
         
         for U in range(len(user)):
            
            if password == user[U]['password']:
                  serializer = Reg_Users_Serializer(user,many=True)
                  
                  return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                  return Response("password",status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

      else:
         return Response("email",status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
      


@api_view(['POST'])
def getData(request):
    
    #player_id = request.POST.get('pid');
    player_id = "P001" 
    Sessions = Training_Session.objects.filter(player_id = player_id).values()
    sessions_list=[]
    
    if Sessions != None:
      for session in Sessions:
         sessions_list.append(session)
        
      return JsonResponse(sessions_list,status=status.HTTP_200_OK,safe=False)
    
    else:
        
      return JsonResponse("",status=status.HTTP_404_NOT_FOUND)
   

   