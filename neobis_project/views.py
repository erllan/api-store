from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializer import (ProductSerializer, CategorySerializer, UserRegisterSerializer, CurtSerializer, AddOrderOnCurt)
from .models import (Product, Category, Curt)
from rest_framework import status

"""User"""


class RegisterUser(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


"""Product"""


class ListCreateProduct(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


"""Category"""


class LisCreateCategory(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


"""Crut"""


class CurtUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        curt = Curt.objects.get(user__id=request.user.id)
        serializer = CurtSerializer(curt)
        return Response(serializer.data)


"""Order"""


class OrderAddToCurt(APIView):
    def post(self, request):
        curt = Curt.objects.get(user__id=request.user.id)
        serializer = AddOrderOnCurt(data=request.data, context={'curt_id': curt.id})
        status_cod = status.HTTP_400_BAD_REQUEST
        if serializer.is_valid():
            serializer.save()
            status_cod = status.HTTP_201_CREATED
        return Response(serializer.data, status=status_cod)
