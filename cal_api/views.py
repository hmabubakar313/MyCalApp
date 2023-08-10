from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from cal_api.serializers import *
from cal_count.models import *
from rest_framework.response import Response



class BreakfastViewSet(APIView):
    def get(self, request, format=None):
        breakfast = Breakfast.objects.all()
        serializer = BreakfastSerializer(breakfast, many=True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serializer = BreakfastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def put(self,request,format=None):
        serializer = BreakfastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    

    def delete(self,request,pk=None,format=None):
        breakfast = Breakfast.objects.get(id=pk)
        breakfast.delete()
        return Response("Item Deleted")


    

class LunchViewSet(APIView):
    def get(self,request,format=None):
        lunch = Lunch.objects.all()
        serializer = LunchSerializer(lunch,many=True)
        return Response(serializer.data)

    
    def post(self,request,format=None):
        serializer = LunchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

    def put(self,request):
        serializer = LunchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    


    def delete(self,request,pk):
        lunch = Lunch.objects.get(id=pk)
        lunch.delete()
        return Response("Item Deleted")



class DinnerViewSet(APIView):
    def get(self,request,format=None):
        dinner = Dinner.objects.all()
        serializer = DinnerSerializer(dinner,many=True)
        return Response(serializer.data)

    
    def post(self,request,format=None):
        serializer = DinnerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

    def put(self,request):
        serializer = DinnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    


    def delete(self,request,pk):
        dinner = Dinner.objects.get(id=pk)
        dinner.delete()
        return Response("Item Deleted")





