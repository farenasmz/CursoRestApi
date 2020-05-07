from rest_framework import viewsets
from .models import *
from rest_framework.decorators import action
from .serializer import ElementSerializer, CategorySerializer, TypeSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail = True, methods=['get'])
    def elements(self, request, pk = none):
        queryset = Element.objects.filter(category_id = pk)
        serializer = ElementSerializer(queryset, many = True)
        return Response(serializer.data)

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(detail = True, methods=['get'])
    def elements(self, request, pk = none):
        queryset = Element.objects.filter(type_id = pk)
        serializer = ElementSerializer(queryset, many = True)
        return Response(serializer.data)