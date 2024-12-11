from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from polutushi.models import Polutushi
from polutushi.api.serializers import PolutushiSerializer
from rest_framework.permissions import IsAuthenticated
from polutushi.tasks import capture_image_from_rtsp


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
      print(request)
      capture_image_from_rtsp.delay(**queryset)
      return Response({"status": "Задача поставлена на выполнение"})
      