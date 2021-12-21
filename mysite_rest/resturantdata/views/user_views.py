from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User

from resturantdata import models

from resturantdata.serializers import ProductSerializers,UserSerializer,UserSerializerWithToken
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   
    def validate(self, attrs):

        data= super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k]=v


        return data
      
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class registerUser(APIView):
    def post(self,request):

        data = request.data
        print(data)
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['username'],
                email=data['email'],
                password=make_password(data['password'])
            )

            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

           
class getUserProfile(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        serializer=UserSerializer(user,many=False)
        return Response(serializer.data)
class getUsers(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user=models.User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
