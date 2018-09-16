from backend.models import Place
from backend.serializers import PlaceSerializer
from rest_framework import generics

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()[:50]
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
