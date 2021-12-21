from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from resturantdata import models
from resturantdata.serializers import ProductSerializers,UserSerializer,UserSerializerWithToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from resturantdata import Product, Review
from resturantdata.serializers import ProductSerializers

from rest_framework import status

class GetProducts(APIView):
    
    
    def get(self,request):
        
        products=models.Products.objects.all()
        response=ProductSerializers(products,many=True)
        return Response(response.data)

class CreateProducts(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        
        product_requset=request.data
        product_data=ProductSerializers(data=product_requset)
        if product_data.is_valid():
            product_data.save()
            return Response({
                'msg':"recived"
            })
        else:
            print(product_data.errors)
            return Response({'error':'product_data.errors'})
            
class getProduct(APIView):
    def get(self,requset,pk):
        product=models.Products.objects.get(id=pk)
        response=ProductSerializers(product,many=False)
        return Response(response.data)
        