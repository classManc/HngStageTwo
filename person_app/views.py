from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PersonSerializer
from .models import Person
# Create your views here.

class CreatePersonView(CreateAPIView):
    serializer_class = PersonSerializer



class RetrievePersonView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
