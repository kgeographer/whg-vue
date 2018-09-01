from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Place
from backend.serializers import PlaceSerializer

@api_view(['GET'])
def place_list(request, format=None):
    """
    List places
    """
    if request.method == 'GET':
        places = Place.objects.all()[:20]
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def place_detail(request, pk, format=None):
    """
    Retrieve a place
    """
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)
