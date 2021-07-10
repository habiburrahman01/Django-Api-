from django.shortcuts import render, redirect
from rest_framework import generics
from .Models.models import soil
from .serializers import SoilSerializer

def index(request):
    return render (request, 'index.html')

def showtable(request):
    context = { 'soil' : soil.objects.all() }
    return render(request,'showtable.html',context)

class SoilList(generics.ListCreateAPIView):
    queryset=soil.objects.all()
    serializer_class=SoilSerializer

class SoilDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=soil
    serializer_class=SoilSerializer