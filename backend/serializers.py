from rest_framework import serializers
from backend.models import Place
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('placeid', 'src_id', 'title', 'dataset')

# ViewSets define the view behavior.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()[:20]
    serializer_class = PlaceSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
