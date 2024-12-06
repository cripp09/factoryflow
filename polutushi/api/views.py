from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from polutushi.models import Polutushi
from polutushi.api.serializers import PolutushiSerializer
from rest_framework.permissions import IsAuthenticated


class PolutushiListView(generics.ListAPIView):
   queryset = Polutushi.objects.all()
   serializer_class = PolutushiSerializer


class PolutushiDetailView(generics.RetrieveAPIView):
   queryset = Polutushi.objects.all()
   serializer_class = PolutushiSerializer


class PolutushaAddView(APIView):
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated]
   def post(self, request, format=None):
      queryset = request.data
      print(queryset)
      Polutushi.objects.create(**queryset)
      return Response({'add': True})