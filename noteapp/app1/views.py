from django.shortcuts import render
from rest_framework import generics
from .models import MyNotes
from .serializer import myNotesSerializer
# Create your views here.
class MyApp(generics.ListCreateAPIView):
    queryset = MyNotes.objects.all()
    serializer_class = myNotesSerializer

class MyAppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyNotes.objects.all()
    serializer_class = myNotesSerializer
