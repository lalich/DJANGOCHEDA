from django.shortcuts import render

# Create your views here.
from .models import Cheeze
from rest_framework import viewsets, permissions
from .serializers import CheezeSerializer

class CheezeViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Todo objects
    queryset = Cheeze.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = CheezeSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]