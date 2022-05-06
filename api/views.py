from django.shortcuts import render
from rest_framework.views import APIView
from owner.models import Books
from api.serializers import BookSerializer
from rest_framework.response import Response
from  rest_framework import status


# Create your views here.

class BooksView(APIView):
    def get(self,request,*args,**kwargs):
        book=Books.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serialzers=BookSerializer(data=request.data)
        if serialzers.is_valid():
            serialzers.save()
            return Response(serialzers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialzers.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        serialzers=BookSerializer(instance=book,data=request.data)
        if serialzers.is_valid():
            serialzers.save()
            return Response(serialzers.data,status=status.HTTP_200_OK)
        else:
            return Response(serialzers.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        book.delete()
        return Response({"message":"deleted"},status=status.HTTP_200_OK)