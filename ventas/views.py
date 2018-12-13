from .models import Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer
from django.shortcuts import render

class ListaProducto(APIView):

    def get(self,request):
        producto  = Producto.objects.all()
        serializer = ProductoSerializer(producto,context={"request":request},many=True)#El many true es porque donde extreamos varias fields son atributos del objectofield
                                                    #sino se pone true este extrae solo un objeto y nosotros estamos extrayendo varios objectos iterables
                                                    
        return Response(serializer.data) 
    def post(self,request):
        pass     