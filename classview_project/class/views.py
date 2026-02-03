from django.shortcuts import render
from .models import Learn_rset
from .serializers import Learn_restSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class info_create(APIView):
    def get(self,request,pk=None, format=None):
        id = pk
        if id is not None:
            ai = Learn_rset.objects.get(id=id)
            serializer = Learn_restSerializer(ai)
            return Response(serializer.data)
        ai = Learn_rset.objects.all()
        serializer = Learn_restSerializer(ai, many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = Learn_restSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully Data insert'})
        return Response(serializer.errors)
    
    def put(self,request,pk,format=None):
        id = pk
        ai = Learn_rset.objects.get(pk=id)
        serializer = Learn_restSerializer(ai,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'full data updated'})
        return Response(serializer.errors)
    def patch(self,request,pk,format=None):
        id = pk
        ai = Learn_rset.objects.get(pk=id)
        serializer = Learn_restSerializer(ai,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'partial data updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk
        ai = Learn_rset.objects.get(pk=id)
        ai.delete()
        return Response({'message':'successfully data deleted'})
    

