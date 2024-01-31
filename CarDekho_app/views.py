from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import CarList,ShowRoomList

from .api_file.serializers import CarSerializer ,ShowRoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
import json

# Create your views here.

# def car_list_view(request):
#     return HttpResponse("<h1>This contains inforamtion about list of Cars</h1>")


                           #without using serializers
# def car_list_view(request):
#     #here first we are taking all the info and storing it in cars and then we are converting it in form of dict and then returning in form of json response
#     cars = CarList.objects.all() 
#     data = {
#         'cars':list(cars.values()), #here we are converting information in form of python dict.
#     }
#     data_json=json.dumps(data)
#     return HttpResponse(data_json,content_type='application/json')
#     # return JsonResponse(data)

# def car_detail_view(request,pk):

#     car=CarList.objects.get(pk=pk)
#     data={
#         'name':car.name,
#         'description':car.description,
#         'active':car.active,
#     }
#     return JsonResponse(data)


                     #using serializers
                        #Class-based Views(the one difference betwwen class and function that in class based we write code inside method that is for get we make get method and write code inside it so we did'nt need to check condition which we have to do in functon based that is (if request.method=='GET' like that)
class showroom_view(APIView):
    def get(self,request):
      showroom = ShowRoomList.objects.all()
      serializer= ShowRoomSerializer(showroom,many=True,context={'request':request})  
      return Response(serializer.data)                     
    
    def post(self,request):
       serializer=ShowRoomSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors)

class showroom_detail_view(APIView):
    def get(self,request,pk):
      try:
         showroom=ShowRoomList.objects.get(pk=pk)
         
      except ShowRoomList.DoesNotExist:
         return Response({"Error":'showroom not found'},status=status.HTTP_404_NOT_FOUND)

      serializer=ShowRoomSerializer(showroom)
      return Response(serializer.data)
    
    def put(self,request,pk):
       showroom=ShowRoomList.objects.get(pk=pk)
       serializer=ShowRoomSerializer(showroom,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
       showroom=ShowRoomList.objects.get(pk=pk)
       showroom.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


              
            
        #  showroom=ShowRoomList.objects.get(pk=pk)
        #  serializer=ShowRoomSerializer(showroom)
        #  if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
      
            
         
               



                 #using serializers
                 # Function Based Views
@api_view(['GET','POST'])
def car_list_view(request):
    if request.method=='GET':
        car = CarList.objects.all()
        serializer = CarSerializer(car,many=True) # many = True means it can contain multiple data but as of now we only have one object that is car. url /car/list(it gives list of all cars)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk): #here we use pk as using particular primary key we want to generate view
    if request.method=='GET':
       try:
        car=CarList.objects.get(pk=pk)
       except:
        return Response({"Error":'car not found'},status=status.HTTP_404_NOT_FOUND)
       serializer=CarSerializer(car) #here we did'nt use many=True, as here we want detail of one car that is in url  /car/1/(it gives info of one car)
       return Response(serializer.data)
    
    if request.method=='PUT':
       car=CarList.objects.get(pk=pk)
       serializer=CarSerializer(car,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    if request.method=='DELETE':
        car=CarList.objects.get(pk=pk)   
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

       